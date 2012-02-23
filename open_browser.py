import sublime, sublime_plugin
import webbrowser

SETTINGS_FILE = "open_browser.sublime-settings"

class OpenBrowserCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		config = sublime.load_settings(SETTINGS_FILE)
		url_map = config.get('path_to_url', {})

		window = sublime.active_window()
		window.run_command('save')
		url = self.view.file_name()
		for path, domain in url_map.items():
			if url.startswith(path):
				url = url.replace(path, domain).replace('\\', '\/')
				break

		webbrowser.open_new(url)