import codecs, encodings
""" Caller will hand this library a buffer string, and ask us to convert
    the buffer, or autodetect what codec the buffer probably uses. """
# 'None' stands for a potentially variable byte ("##" in the XML spec...)
autodetect_dict={ # bytepattern          : ("name",
                (0x00, 0x00, 0xFE, 0xFF) : ("ucs4_be"),
                (0xFF, 0xFE, 0x00, 0x00) : ("ucs4_le"),
                (0xFE, 0xFF, None, None) : ("utf_16_be"),
                (0xFF, 0xFE, None, None) : ("utf_16_le"),
                (0x00, 0x3C, 0x00, 0x3F) : ("utf_16_be"),
                (0x3C, 0x00, 0x3F, 0x00) : ("utf_16_le"),
                (0x3C, 0x3F, 0x78, 0x6D) : ("utf_8"),
                (0x4C, 0x6F, 0xA7, 0x94) : ("EBCDIC"),
                }
def autoDetectXMLEncoding(buffer):
    """ buffer -> encoding_name
        The buffer string should be at least four bytes long.
        Returns None if encoding cannot be detected.
        Note that encoding_name might not have an installed
        decoder (e.g., EBCDIC)
    """
    # A more efficient implementation would not decode the whole
    # buffer at once, but then we'd have to decode a character at
    # a time looking for the quote character, and that's a pain
    encoding = "utf_8" # According to the XML spec, this is the default
                       # This code successively tries to refine the default:
                       # Whenever it fails to refine, it falls back to
                       # the last place encoding was set
    bytes = byte1, byte2, byte3, byte4 = map(ord, buffer[0:4])
    enc_info = autodetect_dict.get(bytes, None)
    if not enc_info: # Try autodetection again, removing potentially
                     # variable bytes
        bytes = byte1, byte2, None, None
        enc_info = autodetect_dict.get(bytes)
    if enc_info:
        encoding = enc_info # We have a guess...these are
                            # the new defaults
        # Try to find a more precise encoding using XML declaration
        secret_decoder_ring = codecs.lookup(encoding)[1]
        decoded, length = secret_decoder_ring(buffer)
        first_line = decoded.split("\n", 1)[0]
        if first_line and first_line.startswith(u"<?xml"):
            encoding_pos = first_line.find(u"encoding")
            if encoding_pos!=-1:
                # Look for double quotes
                quote_pos = first_line.find('"', encoding_pos)
                if quote_pos==-1:                 # Look for single quote
                    quote_pos = first_line.find("'", encoding_pos)
                if quote_pos>-1:
                    quote_char = first_line[quote_pos]
                    rest = first_line[quote_pos+1:]
                    encoding = rest[:rest.find(quote_char)]
    return encoding
