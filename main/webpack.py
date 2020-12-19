from webpack_loader.loader import WebpackLoader

class CustomWebpackLoader(WebpackLoader):
    def filter_chunks(self, chunks):
        chunks = [chunk if isinstance(chunk, dict) else {'name': chunk} for chunk in chunks]
        return super().filter_chunks(chunks)
