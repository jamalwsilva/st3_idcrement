import sublime, sublime_plugin


class St3IdcrementCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        last = None

        for index, region in enumerate(view.sel()):
            text = view.substr(region)

            try:
                number = int(float(text if last is None else last)) + 1
            except:
                number = 0

            view.replace(edit, region, str(number))

            last = number
