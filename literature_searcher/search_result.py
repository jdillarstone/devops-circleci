import subprocess
import tempfile
from re import search
from flask import Blueprint, request, render_template, flash, send_file
from literature_searcher import query_processor

bp = Blueprint("search_result", __name__)

@bp.route("/search_result", methods=["GET", "POST"])
def response():
    query = request.form["search_query"]
    if not query:
        flash("No query")
    search_results = query_processor.process(query)
    results_string = "".join(search_results)
    results_bytes = bytes(results_string, 'utf-8')

    if request.method == "POST":
        
        # Forwarding to blank page if search query didn't match any database entry (per original spec)
        if results_string == "":
            return render_template("search_result.html", search_results=search_results)  
        
        # Discerning what mimetype the user wants the file downloaded in
        if request.form["download_format"] == "HTML":
            mimetype = 'text/html'
            suffix = ".html"
        else:
            mimetype = 'text/markdown'
            suffix = ".md"

        # Writing search results to a temporary file
        tmp = tempfile.NamedTemporaryFile(suffix=suffix)
        tmp.write(results_bytes)
        tmp.seek(0)

        # Sending file to the user
        if request.form["download_format"] != "PDF":
            return send_file(tmp, mimetype=mimetype, as_attachment=True, download_name="output" + suffix)
        else:
            tmp_pdf = tempfile.NamedTemporaryFile(suffix='.pdf')
            result = subprocess.run(['pandoc', tmp.name, '-o', tmp_pdf.name])
            return send_file(tmp_pdf, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')