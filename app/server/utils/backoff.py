import json
import logging
import random
import time

from apiclient.errors import HttpError


def backoff_exec(request, retries=20, raiseExceptions=None, skipInternalError=False):
    """
    Execute the given httpRequest. Retry (at most 'retries' times) if its response isn't a 200
    or an allowed status code.

    Args:
        request: the request
        retries(int): maximum number of tries to get result
        raiseExceptions(list): a list of http status codes that shouldn't be intercepted. Default: [404]
        skipInternalError: ignore HttpError/500

    Raises:
        Several kinds of exceptions (HttpError and alia)
    """
    exception = Exception("Exponential backoff retry limit reached.")
    if not raiseExceptions:
        raiseExceptions = [404]

    if skipInternalError:
        raiseExceptions.append(500)

    for n in xrange(retries):
        try:
            return request.execute()
        except HttpError as exception:
            try:
                error = json.loads(exception.content).get('error', '')
            except (ValueError, TypeError):
                error = {'errors': [{'reason': exception.content}], 'code': exception.resp.status}

            if error.get('code', '') not in raiseExceptions:
                logging.warn(
                    u"Exponential backoff %s (HttpError : %s - Reason : %s) : %s", n, error.get('code', ''),
                    error.get('errors')[0].get('reason', '') if error.get('errors') else '', exception
                )
                # Apply exponential backoff
                time.sleep(min(2 ** n, 20) + random.randint(0, 1000) / 1000.)
            else:
                # Raise any errors in raiseExceptions
                raise exception

        except Exception as exception:
            if ("Deadline exceeded" in unicode(exception) or "Unable to fetch" in unicode(exception) or
                    "urlfetch.Fetch()" in unicode(exception)):
                logging.warn(u"Exponential backoff %s (Exception) : %s", n, exception)

                # Apply exponential backoff.
                time.sleep(min(2 ** n, 20) + random.randint(0, 1000) / 1000.)
            else:
                # Other error, re-raise.
                raise

    # Raise any other errors not caught
    raise exception
