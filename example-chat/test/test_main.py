from p2pit_chat_example import parse_args


def test_default_bootstrap():
    """
    Expect that we have a default bootstrap with at least one host
    """
    args = parse_args([])

    assert "bootstrap" in args
    assert len(args.bootstrap)
    assert len(args.bootstrap[0]) == 2

    assert isinstance(args.bootstrap[0][0], str)
    assert isinstance(args.bootstrap[0][1], int)


def test_accept_multiple_hosts():
    """
    Multiple hosts are allowed
    """
    expected_hosts = ["localhost", "yokeljokes", "smokel.toast"]
    hosts_str = ",".join(expected_hosts)

    args = parse_args([f"--bootstrap={hosts_str}"])

    actual_hosts = [host for host, _port in args.bootstrap]

    assert expected_hosts == actual_hosts


def test_main():
    raise NotImplementedError()
