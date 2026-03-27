import os
import json

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

PORT = int(os.environ.get("MTPROTO_PORT", 443))

# name -> secret (32 hex chars)
# Can be set via env: MTPROTO_SECRET=<32 hex chars>
USERS = {
    "tg": os.environ.get("MTPROTO_SECRET", "90f1cdecf45ef2210411b4eb154fad0c"),
}

# Can be set via env: MTPROTO_MODES='{"classic": false, "secure": false, "tls": true}'
_modes_env = os.environ.get("MTPROTO_MODES")
MODES = json.loads(_modes_env) if _modes_env else {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# Can be set via env: MTPROTO_TLS_DOMAIN=www.google.com
_tls_domain = os.environ.get("MTPROTO_TLS_DOMAIN")
if _tls_domain:
    TLS_DOMAIN = _tls_domain

# Tag for advertising, obtainable from @MTProxybot
# Can be set via env: MTPROTO_AD_TAG=3c09c680b76ee91a4c25ad51f742267d
_ad_tag = os.environ.get("MTPROTO_AD_TAG")
if _ad_tag:
    AD_TAG = _ad_tag
