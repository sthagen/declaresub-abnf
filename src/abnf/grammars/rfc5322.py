"""
Collected rules from RFC 5322
https://tools.ietf.org/html/rfc5322
"""

from ..parser import Rule as _Rule
from .misc import load_grammar_rules


@load_grammar_rules()
class Rule(_Rule):
    """Rule objects generated from ABNF in RFC 5322."""

    grammar = [
        'quoted-pair = ("\\" (VCHAR / WSP)) / obs-qp',
        "FWS = ([*WSP CRLF] 1*WSP) / obs-FWS ",
        "ctext = %d33-39 / %d42-91 / %d93-126 / obs-ctext",
        "ccontent = ctext / quoted-pair / comment",
        'comment = "(" *([FWS] ccontent) [FWS] ")"',
        "CFWS = (1*([FWS] comment) [FWS]) / FWS",
        'atext = ALPHA / DIGIT / "!" / "#" / "$" / "%" / "&" / "\'" / "*" / "+" / "-" / "/" / "=" / "?" / "^" / "_" / "`" / "{" / "|" / "}" / "~"',
        "atom = [CFWS] 1*atext [CFWS]",
        'dot-atom-text = 1*atext *("." 1*atext)',
        "dot-atom = [CFWS] dot-atom-text [CFWS]",
        'specials = "(" / ")" / "<" / ">" / "[" / "]" / ":" / ";" / "@" / "\\" / "," / "." / DQUOTE',
        "qtext = %d33 / %d35-91 / %d93-126 / obs-qtext",
        "qcontent = qtext / quoted-pair",
        "quoted-string = [CFWS] DQUOTE *([FWS] qcontent) [FWS] DQUOTE [CFWS]",
        "word = atom / quoted-string",
        "phrase = 1*word / obs-phrase",
        "unstructured = (*([FWS] VCHAR) *WSP) / obs-unstruct",
        'date-time = [ day-of-week "," ] date time [CFWS]',
        "day-of-week = ([FWS] day-name) / obs-day-of-week",
        'day-name = "Mon" / "Tue" / "Wed" / "Thu" / "Fri" / "Sat" / "Sun"',
        "date = day month year",
        "day = ([FWS] 1*2DIGIT FWS) / obs-day",
        'month = "Jan" / "Feb" / "Mar" / "Apr" / "May" / "Jun" / "Jul" / "Aug" / "Sep" / "Oct" / "Nov" / "Dec"',
        "year = (FWS 4*DIGIT FWS) / obs-year",
        "time = time-of-day zone",
        'time-of-day = hour ":" minute [ ":" second ]',
        "hour = 2DIGIT / obs-hour",
        "minute = 2DIGIT / obs-minute",
        "second = 2DIGIT / obs-second",
        'zone = (FWS ( "+" / "-" ) 4DIGIT) / obs-zone',
        "address = mailbox / group",
        "mailbox = name-addr / addr-spec",
        "name-addr = [display-name] angle-addr",
        'angle-addr = [CFWS] "<" addr-spec ">" [CFWS] / obs-angle-addr',
        'group = display-name ":" [group-list] ";" [CFWS]',
        "display-name = phrase",
        'mailbox-list = (mailbox *("," mailbox)) / obs-mbox-list',
        'address-list = (address *("," address)) / obs-addr-list',
        "group-list = mailbox-list / CFWS / obs-group-list",
        'addr-spec = local-part "@" domain',
        "local-part = dot-atom / quoted-string / obs-local-part",
        "domain = dot-atom / domain-literal / obs-domain",
        'domain-literal = [CFWS] "[" *([FWS] dtext) [FWS] "]" [CFWS]',
        "dtext = %d33-90 / %d94-126 / obs-dtext ",
        "message = (fields / obs-fields) [CRLF body]",
        "body = (*(*998text CRLF) *998text) / obs-body",
        "text = %d1-9 / %d11 / %d12 / %d14-127",
        "fields = *(trace *optional-field / *(resent-date / resent-from / resent-sender / resent-to / resent-cc / resent-bcc / resent-msg-id)) *(orig-date / from / sender / reply-to / to / cc / bcc / message-id / in-reply-to / references / subject / comments / keywords / optional-field)",
        'orig-date = "Date:" date-time CRLF',
        'from = "From:" mailbox-list CRLF',
        'sender = "Sender:" mailbox CRLF',
        'reply-to = "Reply-To:" address-list CRLF',
        'to = "To:" address-list CRLF',
        'cc = "Cc:" address-list CRLF',
        'bcc = "Bcc:" [address-list / CFWS] CRLF',
        'message-id = "Message-ID:" msg-id CRLF',
        'in-reply-to = "In-Reply-To:" 1*msg-id CRLF',
        'references = "References:" 1*msg-id CRLF',
        'msg-id = [CFWS] "<" id-left "@" id-right ">" [CFWS]',
        "id-left = dot-atom-text / obs-id-left",
        "id-right = dot-atom-text / no-fold-literal / obs-id-right",
        'no-fold-literal = "[" *dtext "]"',
        'subject = "Subject:" unstructured CRLF',
        'comments = "Comments:" unstructured CRLF',
        'keywords = "Keywords:" phrase *("," phrase) CRLF',
        'resent-date = "Resent-Date:" date-time CRLF',
        'resent-from = "Resent-From:" mailbox-list CRLF',
        'resent-sender = "Resent-Sender:" mailbox CRLF',
        'resent-to = "Resent-To:" address-list CRLF',
        'resent-cc = "Resent-Cc:" address-list CRLF',
        'resent-bcc = "Resent-Bcc:" [address-list / CFWS] CRLF',
        'resent-msg-id = "Resent-Message-ID:" msg-id CRLF',
        "trace = [return] 1*received",
        'return = "Return-Path:" path CRLF',
        'path = angle-addr / ([CFWS] "<" [CFWS] ">" [CFWS])',
        'received = "Received:" *received-token ";" date-time CRLF',
        "received-token = word / angle-addr / addr-spec / domain",
        'optional-field = field-name ":" unstructured CRLF',
        "field-name = 1*ftext",
        "ftext = %d33-57 / %d59-126 ",
        "obs-NO-WS-CTL = %d1-8 / %d11 / %d12 / %d14-31 / %d127 ",
        "obs-ctext = obs-NO-WS-CTL",
        "obs-qtext = obs-NO-WS-CTL",
        "obs-utext = %d0 / obs-NO-WS-CTL / VCHAR",
        'obs-qp = "\\" (%d0 / obs-NO-WS-CTL / LF / CR)',
        "obs-body = *((*LF *CR *((%d0 / text) *LF *CR)) / CRLF)",
        "obs-unstruct = *((*LF *CR *(obs-utext *LF *CR)) / FWS)",
        'obs-phrase = word *(word / "." / CFWS)',
        'obs-phrase-list = [phrase / CFWS] *("," [phrase / CFWS])',
        "obs-FWS = 1*WSP *(CRLF 1*WSP)",
        "obs-day-of-week = [CFWS] day-name [CFWS]",
        "obs-day = [CFWS] 1*2DIGIT [CFWS]",
        "obs-year = [CFWS] 2*DIGIT [CFWS]",
        "obs-hour = [CFWS] 2DIGIT [CFWS]",
        "obs-minute = [CFWS] 2DIGIT [CFWS]",
        "obs-second = [CFWS] 2DIGIT [CFWS]",
        'obs-zone = "UT" / "GMT" / "EST" / "EDT" / "CST" / "CDT" / "MST" / "MDT" / "PST" / "PDT" / %d65-73 / %d75-90 / %d97-105 / %d107-122 ',
        'obs-angle-addr = [CFWS] "<" obs-route addr-spec ">" [CFWS]',
        'obs-route = obs-domain-list ":"',
        'obs-domain-list = *(CFWS / ",") "@" domain *("," [CFWS] ["@" domain])',
        'obs-mbox-list = *([CFWS] ",") mailbox *("," [mailbox / CFWS])',
        'obs-addr-list = *([CFWS] ",") address *("," [address / CFWS])',
        'obs-group-list = 1*([CFWS] ",") [CFWS]',
        'obs-local-part = word *("." word)',
        'obs-domain = atom *("." atom)',
        "obs-dtext = obs-NO-WS-CTL / quoted-pair",
        "obs-fields = *(obs-return / obs-received / obs-orig-date / obs-from / obs-sender / obs-reply-to / obs-to / obs-cc / obs-bcc / obs-message-id / obs-in-reply-to / obs-references / obs-subject / obs-comments / obs-keywords / obs-resent-date / obs-resent-from / obs-resent-send / obs-resent-rply / obs-resent-to / obs-resent-cc / obs-resent-bcc / obs-resent-mid / obs-optional)",
        'obs-orig-date = "Date" *WSP ":" date-time CRLF',
        'obs-from = "From" *WSP ":" mailbox-list CRLF',
        'obs-sender = "Sender" *WSP ":" mailbox CRLF',
        'obs-reply-to = "Reply-To" *WSP ":" address-list CRLF',
        'obs-to = "To" *WSP ":" address-list CRLF',
        'obs-cc = "Cc" *WSP ":" address-list CRLF',
        'obs-bcc = "Bcc" *WSP ":" (address-list / (*([CFWS] ",") [CFWS])) CRLF',
        'obs-message-id = "Message-ID" *WSP ":" msg-id CRLF',
        'obs-in-reply-to = "In-Reply-To" *WSP ":" *(phrase / msg-id) CRLF',
        'obs-references = "References" *WSP ":" *(phrase / msg-id) CRLF',
        "obs-id-left = local-part",
        "obs-id-right = domain",
        'obs-subject = "Subject" *WSP ":" unstructured CRLF',
        'obs-comments = "Comments" *WSP ":" unstructured CRLF',
        'obs-keywords = "Keywords" *WSP ":" obs-phrase-list CRLF',
        'obs-resent-from = "Resent-From" *WSP ":" mailbox-list CRLF',
        'obs-resent-send = "Resent-Sender" *WSP ":" mailbox CRLF',
        'obs-resent-date = "Resent-Date" *WSP ":" date-time CRLF',
        'obs-resent-to = "Resent-To" *WSP ":" address-list CRLF',
        'obs-resent-cc = "Resent-Cc" *WSP ":" address-list CRLF',
        'obs-resent-bcc = "Resent-Bcc" *WSP ":" (address-list / (*([CFWS] ",") [CFWS])) CRLF',
        'obs-resent-mid = "Resent-Message-ID" *WSP ":" msg-id CRLF',
        'obs-resent-rply = "Resent-Reply-To" *WSP ":" address-list CRLF',
        'obs-return = "Return-Path" *WSP ":" path CRLF',
        'obs-received = "Received" *WSP ":" *received-token CRLF',
        'obs-optional = field-name *WSP ":" unstructured CRLF',
    ]
