# -*- coding: utf-8 -*-

# Copyright © 2012-2014 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from docutils import nodes
from docutils.parsers.rst import Directive, directives
from random import randrange

from nikola.plugin_categories import RestExtension
#from nikola import req_missing


class Plugin(RestExtension):

    name = "rest_playlists"

    def set_site(self, site):
        self.site = site
        directives.register_directive('playlist', Media)
        return super(Plugin, self).set_site(site)


class Media(Directive):
    has_content = False
    required_arguments = 1
    optional_arguments = 0

    def run(self):
        playlist_id = 'playlist-' + str(randrange(0, 10**6))
        src = self.arguments[0].replace('"', '\\"')
        html = """
            <div id="%s"></div>
            <script type="text/javascript">
                $(document).ready(function(){
                    make_playlist($("#%s"), "%s");
                });
            </script>""" % (playlist_id, playlist_id, src)
        return [nodes.raw('', html, format='html')]
