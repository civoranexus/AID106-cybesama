from enum import Enum

class Intent(str, Enum):
    SCHEME_ELIGIBILITY = "scheme_eligibility"
    SCHEME_INFO = "scheme_info"
    DOCUMENTS_REQUIRED = "documents_required"
    APPLICATION_PROCESS = "application_process"
    SMALL_TALK = "small_talk"
    OUT_OF_SCOPE = "out_of_scope"
