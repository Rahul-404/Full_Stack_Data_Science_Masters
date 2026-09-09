### Step 5. First Nix Build

Now that we have our initial `flake.nix` and `configuration.nix`, it's time to build and apply our configuration to the Mac.

First, let's make sure our configuration files are tracked by Git:

```bash
git add .
```

> Git tracking is not required for Nix to build the configuration, but keeping our configuration under version control is important for reproducibility, history, and recovery.

Now we can build and activate our nix-darwin configuration:

```bash
sudo nix run nix-darwin -- switch --flake ~/.dotfiles#mac
```

Let's break this command down:

```text
sudo
  ↓
run with administrator privileges

nix run nix-darwin
  ↓
run nix-darwin

switch
  ↓
build and activate the configuration

--flake ~/.dotfiles#mac
  ↓
use the "mac" configuration from our flake
```

Nix will evaluate our configuration, download any required dependencies, build the system configuration, and activate it on the current Mac.

The first build can take some time because Nix may need to download and build dependencies that aren't already available on the system. Be patient and allow the process to finish.

Once the configuration has been successfully activated, our Mac is now being managed by our declarative nix-darwin configuration.

### Rebuilding after configuration changes

Whenever we modify our Nix configuration, we need to build and activate the updated configuration again.

For example, if we change:

```text
configuration.nix
```

we need to run:

```bash
sudo nix run nix-darwin -- switch --flake ~/.dotfiles#mac
```

Doing this manually every time is repetitive, so let's create a small helper script.

Create:

```bash
vim rebuild.sh
```

Add:

```bash
#!/usr/bin/env bash

set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"

ln -sfn "$DIR" ~/.dotfiles

exec sudo nix run nix-darwin -- switch --flake ~/.dotfiles#mac
```

The script does two things:

1. Ensures that `~/.dotfiles` points to our current dotfiles repository.
2. Runs the nix-darwin rebuild command using our flake.

Make the script executable:

```bash
chmod +x rebuild.sh
```

From now on, whenever we make changes to our Nix configuration, we can simply run:

```bash
./rebuild.sh
```

Enter the administrator password when prompted, and nix-darwin will build and activate the updated configuration.

Our workflow is now:

```text
Edit configuration
       ↓
./rebuild.sh
       ↓
Nix evaluates the flake
       ↓
Nix builds the configuration
       ↓
nix-darwin activates it
       ↓
macOS updated
```

This gives us a simple and repeatable way to apply changes to our system configuration.
