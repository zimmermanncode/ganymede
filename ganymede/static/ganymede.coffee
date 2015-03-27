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
        @$_ = $('#ganymede')
        if not @$_.length
            @$_ = $('<div id="ganymede"></div>')
        $('body').append @$_

        @$_logo = $('#ganymede-logo')
        if not @$_logo.length
            @$_logo = $('<img id="ganymede-logo" />')
        @$_.append @$_logo
        @$_logo[0].src = "#{logo_src}"
        @$_logo.addClass('ui-resizable-handle ui-resizable-se')

        @$_.append @$_menubar = $('#menubar')
        @$_.append @$_toolbar = $('#maintoolbar')

        @prevent_toggle = false
        @$_.resizable
            handles:
                se: @$_logo
            resize: =>
                @prevent_toggle = true
                @update()
        @$_logo.off 'click'
        @$_logo.click =>
            if @prevent_toggle
                @prevent_toggle = false
                return
            if @vertical
                @$_.css
                    width: if @$_.outerWidth() != @width
                        @width
                    else
                        @$_logo.outerWidth true
            else
                @$_.css
                    height: if @$_.outerHeight() != @height
                        @height
                    else
                        @$_logo.outerHeight true
        @update()

        @$_console = $('#ipython-main-app')
        @$_console.append @$_notifier = $('#notification_area')
        @$_console.handles = handles = {}
        for handle in ['sw', 's', 'se']
            id = "ganymede-console-handle-#{handle}"
            $_ = $('#' + id)
            if not $_.length
                $_ = $("""<div id="#{id}">. . .</div>""")
            $_.addClass """ganymede-console-handle btn btn-default
                ui-resizable-handle ui-resizable-#{handle}
                """
            @$_console.append handles[handle] = $_
        @preventConsoleToggle = false
        @$_console.resizable
            handles: handles
            start: (event) ->
                @mouseX = event.pageX
                @offsetX = $(@).offset().left
            resize: (event) ->
                if $(@).data('ui-resizable').axis == 's'
                    $(@).css
                        left: @offsetX + event.pageX - @mouseX
            stop: =>
                @preventConsoleToggle = true
        handle = @$_console.handles.s
        handle.off 'click'
        handle.click =>
            if @preventConsoleToggle
                @preventConsoleToggle = false
                return
            @$_console.toggleClass 'collapsed'
            if @$_console.hasClass 'collapsed'
                @consoleHeight = @$_console.outerHeight()
                @$_console.height 0
            else
                @$_console.height @consoleHeight

        @$_tabs = $('#ganymede-console-tabs')
        if not @$_tabs.length
            @$_tabs = $('<ul id="ganymede-console-tabs"></ul>')
        $_tab = $('<li><a href="#notebook"></a></li>')
        $_ = $('#kernel_indicator')
        $('a', $_tab).append $_
        $('.kernel_indicator_name', $_).hide()
        $_.prepend $('#notebook_name')
        $_.prepend $('#kernel_logo_widget')
        @$_tabs.empty().append $_tab
        @$_console.append @$_tabs
        @$_console.tabs()

        $('#notebook-container').resize ->
            $('.output_wrapper', @).draggable
                handle: '.out_prompt_overlay'
                start: ->
                    $_console = window.ganymede.$_console
                    window.ganymede.consoleHeight = $_console.outerHeight()
                    $_console.height 0
                    $_console.addClass 'collapsed'
                    $_ = $(@)
                    $_.addClass 'ganymede'
                    $_.css 'z-index', 999
                    $_outputs = $('.output_wrapper.ganymede').sort (l, r) ->
                        ($(l).css 'z-index') - ($(r).css 'z-index')
                    for output, index in $_outputs
                        $(output).css 'z-index', 200 + index
                    $_.css 'z-index', 200 + index
                stop: ->
                    $_console = window.ganymede.$_console
                    $_console.height window.ganymede.consoleHeight
                    $_console.removeClass 'collapsed'

    update: ->
        @width = @$_.outerWidth()
        @height = @$_.outerHeight()
        @horizontal = not (@vertical = @$_.outerHeight() > @$_.outerWidth())
        for $_ in [@$_menubar, @$_toolbar]
            $_.toggleClass 'vertical', @vertical
            $_.toggleClass 'horizontal', @horizontal
        $_groups = $('.btn-group', @$_toolbar)
        if @horizontal
            group_widths = for group in $_groups
                $_buttons = $('.btn', group)
                width = 6 + $_buttons.length * ($_buttons.outerWidth true)
                $(group).css
                    width: width
                $(group).outerWidth true
            @$_toolbar.css
                width: group_widths.reduce (l, r) -> l + r
        else
            $_groups.css
                width: ''
            @$_toolbar.css
                width: ''
        @
