### 4. Setting up nix-darwin

Now that Nix is installed and our dotfiles repository is ready, we can start defining our macOS configuration.

For this, we'll use **[nix-darwin](https://github.com/nix-darwin/nix-darwin)**. nix-darwin allows us to manage macOS system configuration declaratively using Nix.

Instead of manually configuring the same settings every time we set up a Mac, we can describe them in configuration files and let nix-darwin apply them for us.

We'll start with the basic nix-darwin flake configuration.

Create a `flake.nix` file:

```bash
vim flake.nix
```

For the initial setup, we can start from the nix-darwin boilerplate configuration and adapt it for our system:

```nix
{
  description = "My macOS system configuration";

  inputs = {
    # Use a stable Nixpkgs release for predictable builds.
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-26.05-darwin";

    # Use the matching nix-darwin release.
    nix-darwin.url = "github:nix-darwin/nix-darwin/nix-darwin-26.05";

    # Make nix-darwin use the same nixpkgs version as our flake.
    nix-darwin.inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = {
    self,
    nix-darwin,
    nixpkgs,
  }: {
    darwinConfigurations."mac" =
      nix-darwin.lib.darwinSystem {
        modules = [
          ./configuration.nix
        ];
      };
  };
}
```

There are two important ideas here.

First, we explicitly choose the Nixpkgs and nix-darwin release branches instead of using an unspecified moving target. This gives us a more predictable configuration and reduces unexpected changes when rebuilding the system.

Second, `nix-darwin.inputs.nixpkgs.follows = "nixpkgs";` tells nix-darwin to use the same `nixpkgs` input that our flake uses, rather than bringing in a separate version.

The flake references another file:

```text
./configuration.nix
```

This is where we'll define the actual macOS configuration.

Create it with:

```bash
vim configuration.nix
```

Add the following initial configuration:

```nix
{ ... }:

{
  # Determinate already manages the Nix installation and daemon,
  # so nix-darwin should not manage them.
  nix.enable = false;

  nixpkgs.config.allowUnfree = true;

  # Apple Silicon Macs use aarch64-darwin.
  # Intel Macs should use x86_64-darwin.
  nixpkgs.hostPlatform = "aarch64-darwin";

  # The primary macOS user.
  system.primaryUser = "rahulshelke";

  # nix-darwin configuration state version.
  system.stateVersion = 6;
}
```

### Understanding the configuration

#### `nix.enable = false`

```nix
nix.enable = false;
```

Determinate Nix is already responsible for installing and managing the Nix daemon on our system.

Therefore, we don't want nix-darwin to attempt to manage the Nix installation as well. Setting this to `false` tells nix-darwin to leave Nix management to Determinate.

#### `nixpkgs.config.allowUnfree`

```nix
nixpkgs.config.allowUnfree = true;
```

Nixpkgs contains both free and non-free software. This option allows us to install packages from Nixpkgs that have licenses classified as unfree.

#### `nixpkgs.hostPlatform`

```nix
nixpkgs.hostPlatform = "aarch64-darwin";
```

This specifies the target platform for our Nix configuration.

Since this Mac uses Apple Silicon, we use:

```text
aarch64-darwin
```

For an Intel Mac, we would use:

```text
x86_64-darwin
```

#### `system.primaryUser`

```nix
system.primaryUser = "rahulshelke";
```

This specifies the primary macOS user for the nix-darwin configuration.

You can find your username with:

```bash
whoami
```

#### `system.stateVersion`

```nix
system.stateVersion = 6;
```

This specifies the nix-darwin configuration state version.

It is **not the version of nix-darwin or Nix itself**. It controls compatibility for stateful configuration behavior. Once you choose a state version for a system, you generally keep it unchanged rather than updating it every time you update Nix or nix-darwin.

---

At this point, we have our first working nix-darwin configuration:

```text
dotfiles/
├── flake.nix
└── configuration.nix
```

The relationship between these files is:

```text
flake.nix
    │
    │ defines inputs and system
    ↓
nix-darwin
    │
    │ loads
    ↓
configuration.nix
    │
    │ defines macOS configuration
    ↓
macOS
```

We now have the foundation for managing our Mac declaratively. In the next step, we'll build and apply this configuration to the system.
