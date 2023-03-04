# Summary

- [Introduction](./introduction.md)

- [Why use the PH editor?](./editor_comparison.md)

- [User Manual](./manual/index.md)
    - [Getting Started](./manual/getting_started.md)
    
    - [Anatomy of the Editor](./manual/editor_anatomy.md)

    - [The Chart Manager](./manual/chart_manager/index.md)
        - [Managing Charts](./manual/chart_manager/manage_charts.md)
        - [Managing Songs](./manual/chart_manager/manage_songs.md)
        - [Verifying and Uploading Songs](./manual/chart_manager/verify_and_upload.md)
    
    - [Saving and Auto-Saving](./manual/saving.md)

    - [Settings and their Managers](./manual/settings/index.md)
        - [Global Settings](./manual/settings/global.md)
        - [Per-Song Settings](./manual/settings/local.md)
        - [Shortcuts](./manual/settings/shortcuts.md)

    - [The Chart Preview](./manual/chart_preview/index.md)
        - [The Grid](./manual/chart_preview/grid.md)
        - [Playtesting a chart](./manual/chart_preview/playtest.md)
        - [Slowdowns and Speedups](./manual/chart_preview/speed_controls.md)
    
    - [The Inspector](./manual/inspector/index.md)
        - [Common Properties](./manual/inspector/properties.md)
        - [Editing Properties](./manual/inspector/editing.md)
        - [Copying Properties](./manual/inspector/copying.md)
    
    - [The Timeline](./manual/timeline/index.md)
        - [The Playhead](./manual/timeline/playhead.md)
        - [Tempo Maps and the Sync Module](./manual/timeline/sync.md)
        - [Layers and Visibility](./manual/timeline/layers.md)
        - [Creating and Selecting Notes](./manual/timeline/creation_and_selection.md)
            - [Modifying Notes](./manual/timeline/modifiers/types.md)
            - [Advanced Selection Tools](./manual/timeline/modifiers/selection.md)
        - [Moving Selections Around](./manual/timeline/move_selection.md)

    - [Arranging Tools](./manual/arrange_module/index.md)
        - [Arranging in the Preview](./manual/arrange_module/preview_tools.md)
        - [Autoplacing](./manual/arrange_module/autoplace.md)
        - [The Arrange Wheel](./manual/arrange_module/arrange_wheel.md)
        - [Arranging in Circles](./manual/arrange_module/circles.md)
        - [Flips and Mirrors](./manual/arrange_module/flips_and_mirrors.md)
        - [Rotations](./manual/arrange_module/rotations.md)
    
    - [Angle Tools](./manual/angles_module/index.md)
        - [Angles and Oscillations](./manual/angles_module/angles_and_oscillations.md)
        - [Editing Angles in the Preview](./manual/angles_module/preview_tools.md)
        - [Automatic Angles](./manual/angles_module/autoangle.md)
        - [Angle Increments](./manual/angles_module/increments.md)
        - [Angle Modifiers](./manual/angles_module/modifiers.md)
    
    - [Multinote Presets](./manual/presets/index.md)
        - [Verticals and Horizontals](./manual/presets/verticals_and_horizontals.md)
        - [Quads](./manual/presets/quads.md)
        - [Triangles](./manual/presets/triangles.md)
    
    - [Managing Events and Lyrics](./manual/events/index.md)
        - [Speed Changes](./manual/events/speed_change.md)
        - [Intro Skip](./manual/events/intro_skip.md)
        - [Lyrics](./manual/events/lyrics.md)
        - [Sections](./manual/events/sections.md)
    
    - [The Scripts Manager](./manual/scripts.md)

    - [Importing Charts](./manual/imports/index.md)
        - [DSC/DIVA Charts](./manual/imports/dsc.md)
        - [F2nd Edits](./manual/imports/edits.md)
        - [PPD Charts](./manual/imports/ppd.md)
        - [CSFM/Comfy Charts](./manual/imports/csfm.md)
        - [MIDI Files](./manual/imports/midi.md)

- [Developer Reference](./developer/index.md)
    - [Scripts and Expressions](./developer/scripts_and_expressions/index.md)
        - [Scripting Reference](./developer/scripts_and_expressions/scripts.md)
        - [Advanced Uses of Expressions](./developer/scripts_and_expressions/expressions.md)
    
    - [Common Data Types](./developer/classes/index.md)
        - [Timing Points](./developer/classes/timing_points/index.md)
            - [HBTimingPoint](./developer/classes/timing_points/HBTimingPoint.md)
            - [HBBaseNote](./developer/classes/timing_points/HBBaseNote.md)
            - [HBNoteData](./developer/classes/timing_points/HBNoteData.md)
            - [HBDoubleNote](./developer/classes/timing_points/HBDoubleNote.md)
            - [HBSustainNote](./developer/classes/timing_points/HBSustainNote.md)
            - [HBTimingChange](./developer/classes/timing_points/HBTimingChange.md)
            - [HBBPMChange](./developer/classes/timing_points/HBBPMChange.md)
            - [HBChartSection](./developer/classes/timing_points/HBChartSection.md)
            - [HBIntroSkipMarker](./developer/classes/timing_points/HBIntroSkipMarker.md)

        - [HBChart](./developer/classes/HBChart.md)
        - [HBSong](./developer/classes/HBSong.md)
        
        - [ScriptRunnerScript](./developer/classes/ScriptRunnerScript.md)

        - [HBEditor](./developer/classes/HBEditor.md)
