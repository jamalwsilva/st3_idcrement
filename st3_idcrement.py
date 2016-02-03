import sublime, sublime_plugin


class St3IdcrementCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        last = None

        for index, region in enumerate(view.sel()):
            text = view.substr(region)

            try:
                number = int(float(text)) + 1
            except:
                number = (last if last != None else index) + 1

            view.replace(edit, region, str(number))

            last = number