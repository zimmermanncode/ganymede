# ganymede
#
# Hacking Jupyter's atmosphere
#
# Copyright (C) 2015 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# ganymede is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ganymede is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ganymede. If not, see <http://www.gnu.org/licenses/>.


class Ganymede
    constructor: (logo_src) ->
        @metadata = window.IPython.notebook.metadata.ganymede ?= {}

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

        @metadata.height ?= @logo.$.outerHeight true
        @metadata.width ?= @logo.$.outerWidth true
        @$.height @metadata.height
        @$.width @metadata.width

        @$.resizable
            handles:
                se: @logo.$
            start: =>
                @preventClick = false
                @metadata.slim = false
                @metadata.height = @$.height()
                @metadata.width = @$.width()
            resize: =>
                @resizing = true
                @preventClick = true
                @metadata.height = @$.height()
                @metadata.width = @$.width()
                @update()
            stop: =>
                @resizing = false
                @update()

        @preventClick = false
        @logo.$.click =>
            if @preventClick
                @preventClick = false
                return

            if @vertical
                @metadata.slim = slim = @$.width() == @metadata.width
                @$.width if not slim
                    @metadata.width
                else
                    @logo.$.outerWidth true
            else
                @metadata.slim = slim = @$.height() == @metadata.height
                @$.height if not slim
                    @metadata.height
                else
                    @logo.$.outerHeight true

        @console = new Ganymede.Console()

        $(window).on 'resize.ganymede', =>
            @update()

        @update()

    update: ->
        overHeight = @metadata.height - @$.height() + (@$.outerHeight true) \
            - $(window).height()
        if overHeight > 0
            @$.height @metadata.height - overHeight
        else if not @resizing
            @$.height @metadata.height
        overWidth = @metadata.width - @$.width() + (@$.outerWidth true) \
            - $(window).width()
        if overWidth > 0
            @$.width @metadata.width - overWidth
        else if not @resizing
            @$.width @metadata.width
        @horizontal = not (@vertical = @$.height() > @$.width())

        if @metadata.slim is true
            if @vertical
                @$.width @logo.$.outerWidth true
            else
                @$.height @logo.$.outerHeight true

        for $bar in [@menubar.$, @toolbar.$]
            $bar.toggleClass 'vertical', @vertical
            $bar.toggleClass 'horizontal', @horizontal

        $toolGroups = $('.btn-group', @toolbar.$)
        if @horizontal
            groupWidths = for group in $toolGroups
                $tools = $('.btn', group)
                width = 6 + $tools.length * ($tools.outerWidth true)
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

    unload: ->
        $origin = $('#menubar-container')
        $origin.append @menubar.unload().$
        $origin.append @toolbar.unload().$

        $checkpoint = @console.$checkpoint.prepend $('#notebook_name')
        $origin = $('#header-container')
        $origin.append $checkpoint
        $origin.append $('#kernel_logo_widget')
        $('#header').show()

        $(window).off 'resize.ganymede'
        @console.unload()
        @$.remove()
        @


class Ganymede.Logo
    constructor: (src) ->
        $('#ganymede-logo').remove()
        @$ = $("""<img id="ganymede-logo" src="#{src}" />""")


class Ganymede.MenuBar
    constructor: ->
        @$ = $('#menubar').detach()

    unload: ->
        $('.container-fluid > *:first', @$).after $('#kernel_indicator')
        $('.container-fluid > *:last', @$).before $('#notification_area')
        $('.kernel_indicator_name').show()
        @


class Ganymede.ToolBar
    constructor: ->
        @$ = $('#maintoolbar').detach()
        @$.find('.btn:contains("CellToolbar")').hide()

    unload: ->
        $('.btn-group').css
            width: ''
        @$.css
            width: ''
        @


class Ganymede.Console
    constructor: ->
        @metadata = (window.IPython.notebook.metadata.ganymede ?= {}) \
            .console ?= {}

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

        @metadata.width ?= @$.width()
        @metadata.height ?= @$.height()
        if @metadata.left?
            @$.css
                left: @metadata.left
        else
            @metadata.left = @$.offset().left
        if @metadata.collapsed is true
            @$.addClass 'collapsed'

        @$.resizable
            handles: @$handles
            start: (event) =>
                @preventClick = false
                @metadata.height = @$.height()
                @metadata.width = @$.width()
                @mouseX = event.pageX
                @offsetX = @$.offset().left
            resize: (event) =>
                @resizing = true
                @metadata.height = @$.height()
                @metadata.width = @$.width()
                if @$.data('ui-resizable').axis == 's'
                    @preventClick = true
                    @$.css
                        left: @metadata.left \
                            = @offsetX + event.pageX - @mouseX
                @update()
            stop: =>
                @resizing = false
                @update()

        @preventClick = false
        @$handles.s.click =>
            if @preventClick
                @preventClick = false
                return

            @$.toggleClass 'collapsed'
            @metadata.collapsed = @$.hasClass 'collapsed'
            @update()

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

        $('#notebook-container').on 'resize.ganymede-console', =>
            @updateOutputs()
        $(window).on 'resize.ganymede-console', =>
            @update()
        @update()

    update: ->
        overWidth = @metadata.width - @$.width() + (@$.outerWidth true) \
            + @$.offset().left - $(window).width()
        if overWidth > 0
            @$.width @metadata.width - overWidth
        else if not @resizing
            @$.width @metadata.width

        if @$.hasClass 'collapsed'
            @$.resizable 'disable'
            @$.removeClass 'ui-resizable-disabled ui-state-disabled'
            @$.css
                top: 0
                height: 0
            return @

        @$.resizable 'enable'
        @$.css
            top: top = @$tabs.outerHeight true
        overHeight = @metadata.height - @$.height() + (@$.outerHeight true) \
            + top + (@$handles.s.outerHeight true) - $(window).height()
        if overHeight > 0
            @$.height @metadata.height - overHeight
        else if not @resizing
            @$.height @metadata.height
        @

    updateOutputs: ->
        zValues = for cell in $('.cell', @$)
            metadata = ($(cell).data('cell').metadata.ganymede ?= {}) \
                .output ?= {}
            if metadata.undocked is true
                $output = $('.output_wrapper', cell)
                $output.addClass 'ganymede'
                $output.css
                    position: 'fixed'
                    'z-index': z = metadata['z-index'] or -1
                    top: metadata.top or 0
                    left: metadata.left or 0
                z
            else
                0
        $('body').css
            'z-index': (Math.min zValues...) - 1

        $('.output_wrapper', @$).draggable
            handle: '.out_prompt_overlay'
            start: (event) =>
                $output = $(event.target)
                @$.addClass 'collapsed'
                @update()
                #HACK: keep current offset...
                if not $output.hasClass 'ganymede'
                    offset = $output.offset()
                    data = $output.data('ui-draggable')
                    data.offset.click.top -= offset.top
                    data.offset.click.left -= offset.left
                #... when switching to position: fixed
                $output.addClass 'ganymede'
                $output.css 'z-index', -1
                $outputs = $('.output_wrapper.ganymede').sort (l, r) ->
                    ($(l).css 'z-index') - ($(r).css 'z-index')
                z = -2 - $outputs.length
                $('body').css 'z-index', z - 1
                for output, index in $outputs
                    metadata = ($(output).parents('.cell')
                        .data('cell').metadata.ganymede ?= {}
                        ).output ?= {}
                    $(output).css
                        'z-index': metadata['z-index'] = z + index
                metadata = ($output.parents('.cell')
                    .data('cell').metadata.ganymede ?= {}
                    ).output ?= {}
                metadata.undocked = true
                $output.css
                    'z-index': metadata['z-index'] = z + index
            stop: (event) =>
                $output = $(event.target)
                metadata = ($output.parents('.cell')
                    .data('cell').metadata.ganymede ?= {}
                    ).output ?= {}
                $.extend metadata, $output.offset()
                @$.removeClass 'collapsed'
                @update()
        @

    unload: ->
        $outputs = $('.output_wrapper', @$).removeClass 'ganymede'
        $outputs.css
            'z-index': ''
            position: ''
            top: ''
            left: ''

        @$tabs.remove()
        for loc, $handle of @$handles
            $handle.remove()

        @$.tabs 'destroy'
        @$.resizable 'destroy'
        @$.css
            position: ''
            left: ''
            top: ''
            width: ''
            height: ''

        $([window, '#notebook-container']).off 'resize.ganymede-console'
        @
