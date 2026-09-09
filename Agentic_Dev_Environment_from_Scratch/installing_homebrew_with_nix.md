## Step 7. Installing Homebrew with Nix

Now that we have nix-darwin managing our macOS settings, the next step is to install the applications we need.

On macOS, many useful applications can be installed through **Homebrew**.

We could simply visit the Homebrew website, copy its installation command, and install it manually. However, that would introduce another manual step when setting up a new machine.

Our goal is to make the entire system reproducible, so we want Homebrew itself to be part of our declarative configuration.

For this, we'll use **[`nix-homebrew`](https://github.com/zhaofengli/nix-homebrew)**. `nix-homebrew` is a Nix module that allows us to install and manage Homebrew through our Nix/nix-darwin configuration.

### Add nix-homebrew to the flake

Open our `flake.nix`:

```bash id="s7k2py"
vim flake.nix
```

First, add `nix-homebrew` as an input:

```nix id="h2g7c1"
nix-homebrew.url = "github:zhaofengli/nix-homebrew";
```

Our inputs will now look like:

```nix id="j9q5rx"
inputs = {
  nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-26.05-darwin";

  nix-darwin.url =
    "github:nix-darwin/nix-darwin/nix-darwin-26.05";

  nix-darwin.inputs.nixpkgs.follows = "nixpkgs";

  nix-homebrew.url =
    "github:zhaofengli/nix-homebrew";
};
```

We also need to make `nix-homebrew` available to our `outputs` function:

```nix id="x4p6kn"
outputs = {
  self,
  nix-darwin,
  nixpkgs,
  nix-homebrew,
}: {
```

If we don't include it here, Nix won't know about the `nix-homebrew` variable when we try to use its module.

Finally, add the nix-homebrew module to our nix-darwin configuration:

```nix id="w2d8qa"
modules = [
  ./configuration.nix
  nix-homebrew.darwinModules.nix-homebrew
];
```

Our flake now knows how to integrate Homebrew into the nix-darwin configuration.

### Configure Homebrew

Now let's return to `configuration.nix`:

```bash id="q3c7vx"
vim configuration.nix
```

Add the following:

```nix id="j2v8lm"
nix-homebrew = {
  enable = true;
  user = "rahulshelke";
};

homebrew = {
  enable = true;

  onActivation.cleanup = "zap";
  onActivation.autoUpdate = true;
  onActivation.extraFlags = [ "--force" ];

  casks = [
    "wezterm"
  ];
};
```

There are two related pieces here.

First:

```nix id="w7k1mh"
nix-homebrew = {
  enable = true;
  user = "rahulshelke";
};
```

This tells nix-darwin to install and manage the Homebrew installation for our user.

Then:

```nix id="8q3c2v"
homebrew = {
  enable = true;
  ...
};
```

configures the packages that Homebrew should manage.

### Homebrew cleanup

One particularly useful setting is:

```nix id="m8v4ka"
onActivation.cleanup = "zap";
```

This tells nix-darwin to clean up Homebrew packages that are not declared in our configuration when the configuration is activated.

This is useful for maintaining reproducibility.

For example, instead of manually installing an application with:

```bash
brew install <some-package>
```

we should declare it in our configuration.

That way, our Git repository becomes the source of truth for the applications installed through Homebrew.

If we want another application, we add it to the appropriate Homebrew package list and rebuild the system.

### Installing our first application

We'll start with **WezTerm**, the terminal emulator we'll use:

```nix id="k4p2qd"
casks = [
  "wezterm"
];
```

Homebrew **casks** are primarily used for macOS graphical applications.

Other GUI applications we want to manage through Homebrew can be added to this list.

For example:

```nix id="7m2q6a"
casks = [
  "wezterm"
  # "another-app"
  # "another-gui-tool"
];
```

The important principle is that we don't want our machine to become a collection of manually installed applications that aren't represented in our configuration.

Instead:

```text id="v8n4cy"
configuration.nix
       ↓
   Homebrew
       ↓
   Applications
```

Our configuration becomes the source of truth.

### Apply the configuration

Now rebuild our system:

```bash id="z6p3dw"
./rebuild.sh
```

nix-darwin will evaluate the configuration, install Homebrew if necessary, and then use the declared Homebrew configuration to install WezTerm.

From this point forward, adding a Homebrew application becomes a simple configuration change followed by:

```bash id="c9r1xk"
./rebuild.sh
```

This is another step toward our goal of having the entire Mac configuration represented as code and reproducible from our Git repository.
