# ganymede
#
# Hacking Jupyter's atmosphere
#
# Copyright (C) 2015 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# ganymede is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ganymede is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ganymede. If not, see <http://www.gnu.org/licenses/>.


class Ganymede
    constructor: (logo_src) ->
        $('#header').hide()
        @menubar = new Ganymede.MenuBar()
        @toolbar = new Ganymede.ToolBar()

        $('#ganymede').remove()
        @$ = $("""<div id="ganymede"></div>""")
        $('body').append @$

        @$.append @menubar.$
        @$.append @toolbar.$

        @logo = new Ganymede.Logo logo_src
        @logo.$.addClass 'ui-resizable-handle ui-resizable-se'
        @$.append @logo.$

        @$.resizable
            handles:
                se: @logo.$
            resize: =>
                @preventClick = true
                @update()

        @logo.$.click =>
            if @preventClick
                @preventClick = false
                return

            if @vertical
                @$.css
                    width: if @$.outerWidth() != @width
                        @width
                    else
                        @logo.$.outerWidth true
            else
                @$.css
                    height: if @$.outerHeight() != @height
                        @height
                    else
                        @logo.$.outerHeight true

        @preventClick = false
        @update()

        @console = new Ganymede.Console()

        $('#notebook-container').resize ->
            $('.output_wrapper', @).draggable
                handle: '.out_prompt_overlay'
                start: ->
                    $console = window.ganymede.console.$
                    if not $console.hasClass 'collapsed'
                        window.ganymede.consoleHeight \
                          = $console.outerHeight()
                        $console.outerHeight 0
                        $console.addClass 'collapsed'
                    $output = $(@)
                    $output.addClass 'ganymede'
                    $output.css 'z-index', -1
                    $outputs = $('.output_wrapper.ganymede').sort (l, r) ->
                        ($(l).css 'z-index') - ($(r).css 'z-index')
                    z = -2 - $outputs.length
                    $('body').css 'z-index', z - 1
                    for output, index in $outputs
                        $(output).css 'z-index', z + index
                    $output.css 'z-index', z + index
                stop: ->
                    $console = window.ganymede.console.$
                    $console.outerHeight window.ganymede.consoleHeight
                    $console.removeClass 'collapsed'

    update: ->
        @width = @$.outerWidth()
        @height = @$.outerHeight()
        @horizontal = not (@vertical = @$.outerHeight() > @$.outerWidth())

        for $bar in [@menubar.$, @toolbar.$]
            $bar.toggleClass 'vertical', @vertical
            $bar.toggleClass 'horizontal', @horizontal

        $toolGroups = $('.btn-group', @toolbar.$)
        if @horizontal
            groupWidths = for group in $toolGroups
                $buttons = $('.btn', group)
                width = 6 + $buttons.length * ($buttons.outerWidth true)
                $(group).css
                    width: width
                $(group).outerWidth true
            @toolbar.$.css
                width: groupWidths.reduce (l, r) -> l + r
        else
            $toolGroups.css
                width: ''
            @toolbar.$.css
                width: ''
        @

    revert: ->
        $origin = $('#menubar-container')
        $origin.append @menubar.revert().$
        $origin.append @toolbar.revert().$

        $checkpoint = @console.$checkpoint.prepend $('#notebook_name')
        $origin = $('#header-container')
        $origin.append $checkpoint
        $origin.append $('#kernel_logo_widget')
        $('#header').show()

        @console.revert()
        @$.remove()
        @


class Ganymede.Logo
    constructor: (src) ->
        $('#ganymede-logo').remove()
        @$ = $("""<img id="ganymede-logo" src="#{src}" />""")


class Ganymede.MenuBar
    constructor: ->
        @$ = $('#menubar').detach()

    revert: ->
        $('.container-fluid *:first', @$).after $('#kernel_indicator')
        $('.kernel_indicator_name').show()
        @


class Ganymede.ToolBar
    constructor: ->
        @$ = $('#maintoolbar').detach()

    revert: ->
        $('.btn-group').css
            width: ''
        @$.css
            width: ''
        @


class Ganymede.Console
    constructor: ->
        @$ = $('#ipython-main-app')
        @$.append @$checkpoint = $('#save_widget')
        @$.append @$notifier = $('#notification_area')

        @$handles = {}
        for loc in ['sw', 's', 'se']
            id = "ganymede-console-handle-#{loc}"
            $('#' + id).remove()
            $handle = $("""<div id="#{id}">. . .</div>""").addClass """
                ganymede-console-handle btn btn-default
                ui-resizable-handle ui-resizable-#{loc}
                """
            @$.append @$handles[loc] = $handle

        @$.resizable
            handles: @$handles
            start: (event) ->
                @mouseX = event.pageX
                @offsetX = $(@).offset().left
            resize: (event) ->
                if $(@).data('ui-resizable').axis == 's'
                    $(@).css
                        left: @offsetX + event.pageX - @mouseX
            stop: =>
                @preventClick = true

        $handle = @$handles.s
        $handle.click =>
            if @preventClick
                @preventClick = false
                return

            @$.toggleClass 'collapsed'
            if @$.hasClass 'collapsed'
                @height = @$.outerHeight()
                @$.height 0
            else
                @$.outerHeight @consoleHeight

        @preventClick = false

        $tab = $('.ganymede-console-tab').detach()
        $('#ganymede-console-tabs').remove()
        @$tabs = $("""<ul id="ganymede-console-tabs"></ul>""")
        if not $tab.length
            $tab = $("""
                <li class="ganymede-console-tab">
                    <a href="#notebook"></a>
                </li>
                """)
            $indicator = $('#kernel_indicator')
            $('a', $tab).append $indicator
            $('.kernel_indicator_name', $indicator).hide()
            $indicator.prepend $('#notebook_name')
            $indicator.prepend $('#kernel_logo_widget')
        @$tabs.append $tab
        @$.prepend @$tabs
        @$.tabs()

    revert: ->
        @$tabs.remove()
        for loc, $handle of @$handles
            $handle.remove()

        $('#notebook').removeClass """ui-tabs-panel
            ui-widget-content ui-corner-bottom
            """
        @$.removeClass """ui-resizable ui-tabs
            ui-widget ui-widget-content ui-corner-all
            """
        @$.css
            left: ''
            top: ''
            width: ''
            height: ''
        @
