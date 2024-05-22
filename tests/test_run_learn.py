"""
Tests for whatshap learn module

"""

import sys

from whatshap.cli.learn import run_learn
import filecmp


def test_run_learn(tmp_path):
    expected = "tests/data/short-genome/learn-data/expected.txt"
    observed = tmp_path / "observed.txt"
    run_learn(
        reference="tests/data/short-genome/learn-data/short_ref.fasta",
        bam="tests/data/short-genome/learn-data/short-reads.bam",
        vcf="tests/data/short-genome/learn-data/variant.vcf",
        k=7,
        window=25,
        output=observed,
    )
    print(observed.read_text(), file=sys.stderr)
    assert filecmp.cmp(expected, observed)
