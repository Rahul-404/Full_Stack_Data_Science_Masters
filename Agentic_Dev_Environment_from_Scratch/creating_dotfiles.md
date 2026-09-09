## Step 3. Creating Dotfiles

Now that Nix is installed, let's create the repository that will contain our system configuration.

Create a directory for our dotfiles:

```bash
mkdir ~/dotfiles
cd ~/dotfiles
```

Initialize it as a Git repository:

```bash
git init
```

We will eventually push this repository to GitHub. This gives us version control for our configuration and allows us to access and restore it from another machine when needed.

Next, create a symbolic link from a fixed location in our home directory to the repository:

```bash
ln -sfn ~/dotfiles ~/.dotfiles
```

This creates:

```text
~/.dotfiles -> ~/dotfiles
```

We use a stable path such as `~/.dotfiles` so that our scripts and configuration can consistently refer to the repository without depending on where the repository itself is stored.

For example, instead of hard-coding:

```text
/Users/rahulshelke/Documents/Data-Science/Data-Science-Projects/dotfiles
```

our scripts can always use:

```text
~/.dotfiles
```

This becomes especially useful when we move the repository to another location or set up the same configuration on another machine.

At this point, we have:

* **Git** initialized for version control.
* **A dotfiles repository** where our configuration will live.
* **A stable `~/.dotfiles` path** that our scripts can reference.
* **Nix** installed and ready to manage our environment.

Next, we'll create our **Nix flake**, which will become the entry point for our reproducible configuration.
