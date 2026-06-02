from dataclasses import dataclass


@dataclass
class CaseResult:
    case_id: str
    passed: bool
    total_assertions: int
    passed_assertions: int