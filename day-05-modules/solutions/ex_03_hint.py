"""Hints for ex_03

    import argparse
    import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None)
    parser.add_argument("--days", type=int, default=7)
    args = parser.parse_args()

    if args.date:
        start = datetime.date.fromisoformat(args.date)
    else:
        start = datetime.date.today()

    delta = datetime.timedelta(days=args.days)
    end = start + delta

    print(f"Start: {start} ({start.strftime('%A')})")
    print(f"Plus {args.days} days: {end} ({end.strftime('%A')})")
"""
