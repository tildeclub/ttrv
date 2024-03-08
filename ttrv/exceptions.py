# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class EscapeInterrupt(Exception):
    "Signal that the ESC key has been pressed"


class ConfigError(Exception):
    "There was a problem with the configuration"


class TTRVError(Exception):
    "Base TTRV error class"


class AccountError(TTRVError):
    "Could not access user account"


class SubmissionError(TTRVError):
    "Submission could not be loaded"


class SubredditError(TTRVError):
    "Subreddit could not be loaded"


class NoSubmissionsError(TTRVError):
    "No submissions for the given page"

    def __init__(self, name):
        self.name = name
        message = '`{0}` has no submissions'.format(name)
        super(NoSubmissionsError, self).__init__(message)


class SubscriptionError(TTRVError):
    "Content could not be fetched"


class InboxError(TTRVError):
    "Content could not be fetched"


class ProgramError(TTRVError):
    "Problem executing an external program"


class BrowserError(TTRVError):
    "Could not open a web browser tab"


class TemporaryFileError(TTRVError):
    "Indicates that an error has occurred and the file should not be deleted"


class MailcapEntryNotFound(TTRVError):
    "A valid mailcap entry could not be coerced from the given url"


class InvalidRefreshToken(TTRVError):
    "The refresh token is corrupt and cannot be used to login"
