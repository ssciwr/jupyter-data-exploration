c = get_config()  # noqa
c.ExecutePreprocessor.enabled = True
c.NbConvertApp.export_format = "slides"
# c.SlidesExporter.extra_template_paths = []
c.SlidesExporter.file_extension = ".html"
c.SlidesExporter.reveal_transition = "convex"
c.SlidesExporter.reveal_scroll = True
# c.SlidesExporter.template_file = None
