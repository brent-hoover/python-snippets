from xml.parsers.xmlproc import utils, xmlval, xmldtd
def validate_xml_file(xml_filename, app=None, dtd_filename=None):
    # build validating parser object with appropriate error handler
    parser = xmlval.Validator()
    parser.set_error_handler(utils.ErrorPrinter(parser))
    if dtd_filename is not None:
        # DTD file specified, load and set it as the DTD to use
        dtd = xmldtd.load_dtd(dtd_filename)
        parser.val.dtd = parser.dtd = parser.ent = dtd
    if app is not None:
        # Application processing requested, set appliation object
        parser.set_application(app)
    # everything being set correctly, finally perform the parsing
    parser.parse_resource(xml_filename)
