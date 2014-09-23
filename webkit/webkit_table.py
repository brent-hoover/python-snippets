#!/usr/bin/env python
#
# [SNIPPET_NAME: Webkit Table]
# [SNIPPET_CATEGORIES: Webkit, PyGTK, csv]
# [SNIPPET_DESCRIPTION: Shows how to load tabular data into a Webkit view]
# [SNIPPET_AUTHOR: Bruno Girin <brunogirin@gmail.com>]
# [SNIPPET_LICENSE: GPL]
#
# This snippet was derived from Andy Breiner's "Webkit Button" snippet and
# Ryan Paul's article at Ars Technica:
# http://arstechnica.com/open-source/guides/2009/07/how-to-build-a-desktop-wysiwyg-editor-with-webkit-and-html-5.ars/
# It demonstrates how to create a HTML table from the content of a CSV file,
# display it in a Webkit view and handle change events from a GTK combo box to
# change the document's style sheet.
#
# The garish colours for the "Colourful" style were generated using:
# http://colorschemedesigner.com/
#
# It's Easter, so this snippet shows details about the nutritional information
# of chocolate, found here: http://www.chokladkultur.se/facts.htm

import csv
import sys

import gtk, gobject
import webkit

class TableData:
    """
    Data model class that encapsulates the content of the CSV file.
    
    This class reads the content of the CSV file, stores the first row as a
    header and the other rows as a list of list representing the content.
    """
    def __init__(self, csv_file):
        reader=csv.reader(open(csv_file))
        self.headers = []
        self.content = []
        for row in reader:
            if reader.line_num == 1:
                self.headers = row
            else:
                self.content.append(row)

class TableView:
    """
    View class that displays the content of the data model class.
    
    This class creates a HTML table from the data held in the model class
    and uses Webkit to display it. It also provides the user with a combo box
    to change the style used to display the table.
    """
    def delete_event(self, widget, event, data=None):
        """Handles delete events and ignores them."""
        return False

    def destroy(self, widget, data=None):
        """Handles the destroy event and quits the application."""
        gtk.main_quit()

    def __init__(self, file_stem, title, data):
        """
        Initialises the view class, creates a HTML document and wires events.
        
        This is the main method in the view class. It initialises all elements
        of the view, creates a HTML document based on the data model and wires
        GTK and Webkit events to handling methods.
        """
        # Create the threads so webkit can run on its own thread
        gobject.threads_init()

        # Store the file stem
        self.file_stem = file_stem
        
        # Setup the window properties
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(True)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # Initialize webkit
        self.web = webkit.WebView()
        
        # listen for clicks of links
        self.web.connect("navigation-requested", self.on_navigation_requested)

        # the %s will be replaced later on
        self.template = """
            <html>
            <head>
                <style>
                {style}
                </style>
            </head>
            {body}
            </html>
        """
        self.body = """
            <body>
                <h1>{title}</h1>
                <div id="content">
                    <table>
                        <thead>
                        {thead}
                        </thead>
                        <tbody>
                        {tbody}
                        </tbody>
                    </table>
                </div>
            </body>
        """
        self.tr = """<tr>{content}</tr>"""
        self.th = """<th scope="{scope}">{content}</th>"""
        self.td = """<td class="{hclass}">{content}</td>"""

        self.document_body = self.create_document_body(title, data)
        document = self.create_document('plain')
        # tell webkit to load local html and this is where the %s will get
        # replaced
        self.web.load_html_string(document, "file:///")
 
        # Create the style combo box
        combobox = gtk.combo_box_new_text()
        combobox.append_text('Plain')
        combobox.append_text('Business')
        combobox.append_text('Rounded')
        combobox.append_text('Colourful')
        combobox.set_active(0)
        combobox.connect('changed', self.changed_style_combo)
        
        # Create a scroll area and add the webkit item
        scroll = gtk.ScrolledWindow()
        scroll.add(self.web)
        
        # Create a vbox and add the combo box and scroll area to it
        vbox = gtk.VBox()
        vbox.pack_start(combobox, False)    # don't expand
        vbox.pack_start(scroll, True, True) # expand and fill
 
        # add the vbox to the window and show all items on the window
        self.window.add(vbox)
        self.window.show_all()
        self.window.move(0, 10)
        self.window.resize(580, 350)

    def create_document_body(self, title, data):
        """
        Create the document's body from the content of the data model.
        
        This method creates the body of the document by inserting headers and
        body row elements in the core template.
        """
        # Create th nodes and wrap them in tr
        thead = self.tr.format(
            content = ''.join(
                [self.th.format(scope = 'col', content = h) for h in data.headers])
        )
        # Create td nodes, wrap the tr nodes and join them
        # The expression used to set the value of hclass is derived from:
        # http://code.activestate.com/recipes/52282-simulating-the-ternary-operator-in-python/
        # For more details on nested list comprehensions, as used below, see:
        # http://docs.python.org/tutorial/datastructures.html#nested-list-comprehensions
        tbody = '\n'.join(
            [self.tr.format(
                content = ''.join([self.td.format(
                    hclass = (i>0 and 'right' or 'left'), content = d
                    ) for i, d in enumerate(l)]))
            for l in data.content]
        )
        # Create the document body and return
        return self.body.format(
            title = title, thead = thead, tbody = tbody)
    
    def create_document(self, style):
        """
        Create the complete document from the body and the style sheet.
        
        This method creates the final document by reading the CSS style sheet
        file and inserting it along with the document body into the template.
        """
        # Load the style sheet
        f = open(
            '{stem}-{style}.css'.format(stem = self.file_stem, style = style), 'r')
        # Apply to the document and return
        return self.template.format(
            style = f.read(), body = self.document_body)

    def changed_style_combo(self, combobox):
        """
        Change the style by re-creating the document from the combo's selection.
        
        This method gets the current value out of the combo box, transforms it
        to lower case and uses the resulting value to re-create the complete
        document with the relevant CSS style sheet. It then re-displays the
        document using the Webkit view.
        """
        model = combobox.get_model()
        index = combobox.get_active()
        style = model[index][0].lower()
        print 'Changing style to {style}'.format(style = model[index][0])
        document = self.create_document(style)
        self.web.load_html_string(document, "file:///")
    
    def on_navigation_requested(self, view, frame, req, data=None):
        """
        Describes what to do when a href link is clicked.
        
        In this case, we ignore all navigation requests, as there are no
        clickable area in the document.
        """
        # As Ryan Paul stated he likes to use the prefix program:/
        uri = req.get_uri()
        if uri.startswith("program:/"):
            print uri.split("/")[1]
        else: 
            return False
        return True
  
    def main(self):
        """Start the main GTK thread."""
        gtk.main()
        

if __name__ == "__main__":
    data = TableData(sys.argv[0].replace('.py', '.csv'))
    view = TableView(
        sys.argv[0].replace('.py', ''),
        "Chocolate's nutritional information", data)
    view.main()
