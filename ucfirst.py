import sublime, sublime_plugin

class UcfirstCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        for sel in self.view.sel() :
            region = self.replaceRegion(self.view, sel)
            self.view.replace(edit, region, self.view.substr(region).capitalize())

    def replaceRegion(self, view, sel):
        str = view.substr(sel)
        if len(str) > 0 :
            return sel
        else :
            return view.word(sel.begin())