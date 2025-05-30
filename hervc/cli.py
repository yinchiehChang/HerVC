import argparse
import subprocess
import os
from datetime import datetime

__version__ = "0.3"

def run_git_command(cmd):
    result = subprocess.run(["git"] + cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Git error: {result.stderr.strip()}")
    else:
        print(result.stdout.strip())

def awaken(args):
    run_git_command(["init"])
    print("🌱 HerVC: Project awakened. Feminist history begins.")

def engrave(args):
    run_git_command(["add", "."])
    run_git_command(["commit", "-m", args.note])
    print(f"📝 Engraved your mark: '{args.note}'")

def offer(args):
    run_git_command(["push"])
    print("🌊 Your offering has flowed to the collective.")

def embrace(args):
    run_git_command(["pull"])
    print("🫂 Embraced the wisdom of your sisters.")

def bloom(args):
    run_git_command(["checkout", "-b", args.name])
    print(f"🌸 A new branch blooms: '{args.name}'")

def interweave(args):
    run_git_command(["merge", args.name])
    print(f"🧶 Interwoven with: '{args.name}'")

def resonate(args):
    run_git_command(["log", "--oneline"])

def version(args):
    print(f"HerVC version {__version__} 💜")

def main():
    parser = argparse.ArgumentParser(description='HerVC - Feminist Git Wrapper')
    subparsers = parser.add_subparsers(dest='command')

    parser_awaken = subparsers.add_parser('awaken', help='🌱 Awaken a new feminist repository')
    parser_awaken.set_defaults(func=awaken)

    parser_engrave = subparsers.add_parser('engrave', help='📝 Leave your feminist mark')
    parser_engrave.add_argument('--note', required=True, help='Commit message')
    parser_engrave.set_defaults(func=engrave)

    parser_offer = subparsers.add_parser('offer', help='🌊 Offer your work to the remote')
    parser_offer.set_defaults(func=offer)

    parser_embrace = subparsers.add_parser('embrace', help='🫂 Embrace updates from others')
    parser_embrace.set_defaults(func=embrace)

    parser_bloom = subparsers.add_parser('bloom', help='🌸 Bloom a new branch')
    parser_bloom.add_argument('name', help='Name of the new branch')
    parser_bloom.set_defaults(func=bloom)

    parser_interweave = subparsers.add_parser('interweave', help='🧶 Interweave with another branch')
    parser_interweave.add_argument('name', help='Name of the branch to merge')
    parser_interweave.set_defaults(func=interweave)

    parser_resonate = subparsers.add_parser('resonate', help='🔮 View commit resonance')
    parser_resonate.set_defaults(func=resonate)

    parser_version = subparsers.add_parser('version', help='Show HerVC version')
    parser_version.set_defaults(func=version)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()