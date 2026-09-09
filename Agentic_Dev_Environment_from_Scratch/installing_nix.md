### Step 2: Installing Nix

**CLI Installation**

Open Terminal and run the following command:

```bash
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | \
  sh -s -- install
```

Follow the prompts shown by the installer and allow the installation to complete.

Once the installation is finished, the installer will provide a command to load Nix into your current shell environment. Run the following command:

```bash
. /nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh
```

This loads Nix's environment variables and commands into the current Terminal session without requiring you to open a new terminal window.

You can verify that Nix is installed successfully with:

```bash
nix --version
```

If the installation was successful, this will print the installed Nix version.

At this point, **Nix is installed and available in our environment**. In the next step, we'll configure nix-darwin to declaratively manage our macOS system.
