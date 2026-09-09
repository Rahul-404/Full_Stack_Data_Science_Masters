## Step 6. Reproducible Mac Settings

So far, we've successfully applied our Nix configuration, but we haven't actually configured any meaningful macOS settings yet.

Now let's use nix-darwin to declaratively configure some of the everyday settings on our Mac.

Open `configuration.nix`:

```bash
vim configuration.nix
```

Add the following to our configuration:

```nix
system.defaults = {
  NSGlobalDomain = {
    AppleInterfaceStyle = "Dark";
    KeyRepeat = 2;                  # Fast key repeat
    InitialKeyRepeat = 15;          # Short delay before repeat
    _HIHideMenuBar = true;          # Auto-hide the menu bar
    AppleShowAllExtensions = true;  # Always show file extensions
  };

  dock.autohide = true;

  finder.FXPreferredViewStyle = "Nlsv";  # List view by default
  finder.CreateDesktop = false;           # Keep the desktop clean

  trackpad.Clicking = true;               # Tap to click
};
```

These settings are now part of our declarative configuration rather than being configured manually through macOS System Settings.

For example:

* `AppleInterfaceStyle = "Dark"` enables Dark Mode.
* `KeyRepeat` and `InitialKeyRepeat` control keyboard repeat behavior.
* `_HIHideMenuBar` hides the macOS menu bar until it is needed.
* `AppleShowAllExtensions` makes file extensions visible in Finder.
* `dock.autohide` automatically hides the Dock.
* `FXPreferredViewStyle = "Nlsv"` makes Finder use List View by default.
* `finder.CreateDesktop = false` prevents files from being displayed directly on the desktop.
* `trackpad.Clicking = true` enables tap-to-click.

Now rebuild the system:

```bash
./rebuild.sh
```

After the rebuild completes, nix-darwin applies these settings to macOS.

You should now see the changes reflected in your system—for example, the Dock will automatically hide, Dark Mode will be enabled, Finder will use List View, and the menu bar will automatically hide.

### Why this is reproducible

The important part is that these settings are no longer just preferences stored on this particular Mac.

They are now represented as code:

```text
configuration.nix
       ↓
    Git repo
       ↓
     flake
       ↓
  nix-darwin
       ↓
      macOS
```

This means that when we set up another compatible Mac, we can apply the same configuration instead of manually configuring each setting again.

More importantly, because the configuration is stored in Git, every change can be tracked, reviewed, and reverted.

We're beginning to treat our **operating-system configuration as code**.
