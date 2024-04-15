#!/usr/bin/env python3
"""
Arguments:
fields: a list of strings representing all fields to obfuscate
redaction: a string representing by what the field will be obfuscated
message: a string representing the log line
separator: a string representing by which character is separating all fields in the log line (message)
"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    return re.sub(r'(?<=^|{})(?:{}=[^{}]+)'.format(separator, '|'.join(fields), separator), redaction, message)
