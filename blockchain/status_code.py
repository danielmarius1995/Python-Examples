class HttpStatusCodes:
    __http_status_codes = []

    def __init__(self):
        self.__http_status_codes = [
            ("unknown", " "),
            ("information_continue", 100),
            ("information_switching_protocols", 101),
            ("information_processing", 102),
            ("success_ok", 200),
            ("success_created", 201),
            ("success_accepted", 202),
            ("success_non_authoritative_information", 203),
            ("success_no_content", 204),
            ("success_reset_content", 205),
            ("success_partial_content", 206),
            ("success_multi_status", 207),
            ("success_already_reported", 208),
            ("success_im_used", 226),
            ("redirection_multiple_choices", 300),
            ("redirection_moved_permanently", 301),
            ("redirection_found", 302),
            ("redirection_see_other", 303),
            ("redirection_not_modified", 304),
            ("redirection_use_proxy", 305),
            ("redirection_switch_proxy", 306),
            ("redirection_temporary_redirect", 307),
            ("redirection_permanent_redirect", 308),
            ("client_error_bad_request", 400),
            ("client_error_unauthorized", 401),
            ("client_error_payment_required", 402),
            ("client_error_forbidden", 403),
            ("client_error_not_found", 404),
            ("client_error_method_not_allowed", 405),
            ("client_error_not_acceptable", 406),
            ("client_error_proxy_authentication_required", 407),
            ("client_error_request_timeout", 408),
            ("client_error_conflict", 409),
            ("client_error_gone", 410),
            ("client_error_length_required", 411),
            ("client_error_precondition_failed", 412),
            ("client_error_payload_too_large", 413),
            ("client_error_uri_too_long", 414),
            ("client_error_unsupported_media_type", 415),
            ("client_error_range_not_satisfiable", 416),
            ("client_error_expectation_failed", 417),
            ("client_error_im_a_teapot", 418),
            ("client_error_misdirection_required", 421),
            ("client_error_unprocessable_entity", 422),
            ("client_error_locked", 423),
            ("client_error_failed_dependency", 424),
            ("client_error_upgrade_required", 426),
            ("client_error_precondition_required", 428),
            ("client_error_too_many_requests", 429),
            ("client_error_request_header_fields_too_large", 431),
            ("client_error_unavailable_for_legal_reasons", 451),
            ("server_error_internal_server_error", 500),
            ("server_error_not_implemented", 501),
            ("server_error_bad_gateway", 502),
            ("server_error_service_unavailable", 503),
            ("server_error_gateway_timeout", 504),
            ("server_error_http_version_not_supported", 505),
            ("server_error_variant_also_negotiates", 506),
            ("server_error_insufficient_storage", 507),
            ("server_error_loop_detected", 508),
            ("server_error_not_extended", 510),
            ("server_error_network_authentication_required", 511)
        ]

    def get_status_code(self, status_string):
        get_code = 0
        for i in self.__http_status_codes:
            if i[0] == status_string:
                get_code = int(i[1])
        return get_code

    def get_status_string(self, status_code):
        get_string = ''
        for i in self.__http_status_codes:
            if i[1] == status_code:
                get_string = i[0]
        return get_string
