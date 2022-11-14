class Event:
    def __init__(self, raw_data: dict) -> None:
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False

    @staticmethod
    def meets_condition_pre(event_data: dict):
        """인터페이스 계약의 사전조건
        ``event_data`` 파라미터가 적절한 형태인지 유효성 검사
        """

        assert isinstance(event_data, dict), f"{event_data} is not a dict"
        for moment in ("before", "after"):
            assert moment in event_data, f"{moment} not in {event_data}"
            assert isinstance(event_data[moment], dict)


class UnknownEvent(Event):
    """데이터만으로 식별할 수 없는 이벤트"""


class LoginEvent(Event):
    """로그인 사용자에 의한 이벤트"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"].get("session") == 0
            and event_data["after"].get("session") == 1
        )


class LogoutEvent(Event):
    """로그아웃 사용자에 의한 이벤트"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"].get("session") == 1
            and event_data["after"].get("session") == 0
        )


class TransactionEvent(Event):
    """시스템에서 발생한 트랜잭션 이벤트"""

    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return event_data["after"].get("transaction") is not None


class SystemMonitor:
    """시스템에서 발생한 이벤트 분류"""

    def __init__(self, event_data: dict) -> None:
        self.event_data = event_data

    def identify_event(self) -> Event:
        Event.meets_condition_pre(self.event_data)
        event_cls = next(
            (
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            UnknownEvent
        )
        return event_cls(self.event_data)


if __name__ == "__main__":
    l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    print(l1.identify_event().__class__.__name__)
    l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    print(l2.identify_event().__class__.__name__)
    l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print(l3.identify_event().__class__.__name__)
    l4 = SystemMonitor({"before": {}, "after": {"transaction": "Tx001"}})
    print(l4.identify_event().__class__.__name__)