# Shortcuts

The Editor has a very extensive list of ***Keyboard Shortcuts***, which can be used to do common operations very fast, increasing productivity. There is a shortcut for almost every button in the editor, alltough not all of them are *set by default*.
Shortcuts are in no way mandatory, and a lot of the things you can do with them have manual versions. This said, it is very useful to learn at least the ones for the things you do most commonly.

## The Shortcuts Manager

In the settings tab lies the ***Shortcut Manager***, which is used to view and edit shortcuts. In it, you will see a list of all the shortcuts, used or unused, alongside of a brief description of what they do. You will also see a button to **reset all shortcuts**.

![The Shortcut Manager](media/shortcuts_manager.png)

If you double click on a shortcut, you will open a dialog to **edit it**. Press any key combinations or mouse buttons to set the new shortcut. You can also press ***Clear*** to remove the shortcut, or ***Reset to default*** to reset it. Once you are done, click *OK*.

![Editing a shortcut](media/editing_shortcut.png)

The valid types of shortcuts are:
* A *key*
* A *mouse button* (wheel up/down counts)
* One of the above, combined with **one or more** of *Control*, *Shift*, *Alt* or *Meta* (The windows key on most keyboards)

## The Shortcut Map

There are a lot of *default bindings* in the editor. Here, you can navigate a map of them, to familiarize yourself with their usage. Keep in mind that not knowing every single one of these is in no way a problem when charting, but this reference is useful even if you dont use most of them.

To navigate the map, hover over a key, which will show a tooltip with the action it corresponds to. You can also click on the *modifier keys* (or hold them on your physical keyboard) to show the commands related to them.

You can ***filter the shortcuts by category*** by using the dropdown in the left. With the middle textbox you can ***search shortcuts***, and the rightmost icons and dropdown are used to ***select the shape and layout of the keyboard***.

<!-- Shortcut Mapper code -->
<link href="/ShortcutMapper/content/stylesheets/style.css" rel="stylesheet">

<div id="mainwrap">
    <div class="inputgroup">
        <select id="context_select" name="context_select" class="chosen-select" title="Filter Shortcuts"></select>
    </div>
    <div class="inputgroup">
        <div id="search">
            <div id="searchbox">
                <input id="searchfield" name="searchfield" placeholder="Search for shortcuts..." />
                <span class="icon"></span>
                <div id="search_results"></div>
            </div>
        </div>
        <div id="mousecontent"></div>
    </div>
    <div class="inputgroup">
        <!-- leave no spaces between buttons -->
        <button id="os_windows" class="os-radiobutton os-windows leftfield" data-os="windows" title="Display a Windows keyboard"><b></b>
        </button><button id="os_osx" class="os-radiobutton os-mac midfield" data-os="mac" title="Display a Mac keyboard"><b></b>
        </button><button id="os_linux" class="os-radiobutton os-linux rightfield" data-os="windows" title="Display a Linux keyboard"><b></b></button>
    </div>
    <div class="inputgroup">
        <select id="keyboardtype_select" name="keyboardtype_select" class="chosen-select keyboard-select" title= "Set the keyboard layout"></select>
    </div>
    <div id="search_blurdetect"></div>
    <div id="shortcuts-content">
        <div id="contentwrap">
            <div id="keycontent"></div>
        </div>
    </div>
</div>
<!-- End of Shortcut Mapper code -->