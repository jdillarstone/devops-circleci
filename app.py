import os
from literature_searcher import create_app

port = int(os.environ.get("PORT", 5000))
app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)