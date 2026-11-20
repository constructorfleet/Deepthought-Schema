from pathlib import Path


class ProbeGenerator:
    name = "m0-probe"
    summary = "M0 external-generator discovery probe."

    def register_cli(self, subparsers) -> None:
        parser = subparsers.add_parser(self.name, help=self.summary)
        commands = parser.add_subparsers(dest="probe_command", required=True)
        build = commands.add_parser("build", help="Write a discovery marker.")
        build.add_argument("--out", type=Path, default=Path("probe-output"))
        build.set_defaults(func=self.run)

    def run(self, args) -> int:
        args.out.mkdir(parents=True, exist_ok=True)
        (args.out / "discovered.txt").write_text("external generator loaded\n")
        print(f"probe generated under {args.out}/")
        return 0
