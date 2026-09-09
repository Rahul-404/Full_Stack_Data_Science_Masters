### Step 1: Reproducibility

The first problem we want to solve with our configuration is **reproducibility**.

Once we have everything configured on our current machine, can we easily apply the same configuration to another machine and reproduce the same development environment? And, in the less likely but very real scenario where something goes seriously wrong and our system becomes unusable, can we rebuild our environment from a known-good configuration instead of starting from scratch?

Our solution to this is **[Nix](https://nixos.org/)**.

Nix is a declarative and reproducible package and configuration management system. It is also the foundation of **NixOS**, a Linux distribution built around Nix, but you don't need to use NixOS to benefit from Nix.

Nix can also be used on other operating systems, including macOS. For macOS, we can use **[Determinate Nix](https://determinate.systems/)**, which provides an installer and tooling for setting up Nix on macOS.

In this project, we'll use Nix together with **nix-darwin** to declaratively manage our macOS configuration, and we'll use a **flake** to define and lock our dependencies. This gives us a reproducible configuration that can be version-controlled and applied to other compatible machines.

We’ll start by installing Determinate Nix using the following commands.