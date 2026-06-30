from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AgentMessage:
    sender: str
    receiver: str
    message_type: str
    content: str
    evidence: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))


class MessageBus:
    def __init__(self) -> None:
        self.messages: list[AgentMessage] = []

    def send(
        self,
        sender: str,
        receiver: str,
        message_type: str,
        content: str,
        evidence: list[str] | None = None,
    ) -> None:
        self.messages.append(
            AgentMessage(
                sender=sender,
                receiver=receiver,
                message_type=message_type,
                content=content,
                evidence=evidence or [],
            )
        )

    def get_messages(self) -> list[dict]:
        return [
            {
                "sender": msg.sender,
                "receiver": msg.receiver,
                "message_type": msg.message_type,
                "content": msg.content,
                "evidence": msg.evidence,
                "created_at": msg.created_at,
            }
            for msg in self.messages
        ]