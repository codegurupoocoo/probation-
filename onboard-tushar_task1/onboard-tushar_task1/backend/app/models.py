from sqlalchemy import Column, String, DateTime, JSON, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy as sa
from .db import Base
import uuid
from datetime import datetime

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    started_at = Column(DateTime(timezone=True), nullable=True)
    status = Column(String, default='draft')

class Recipient(Base):
    __tablename__ = "recipients"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"), nullable=False)
    name = Column(String)
    email = Column(String)
    extra = Column(JSON, nullable=True)
    sent_at = Column(DateTime(timezone=True), nullable=True)
    delivered_at = Column(DateTime(timezone=True), nullable=True)
    opened_at = Column(DateTime(timezone=True), nullable=True)
    clicked_at = Column(DateTime(timezone=True), nullable=True)
    reminder_sent_at = Column(DateTime(timezone=True), nullable=True)
    status = Column(String, default='pending')

class Event(Base):
    __tablename__ = "events"
    id = Column(sa.Integer, primary_key=True, autoincrement=True)
    recipient_id = Column(UUID(as_uuid=True), ForeignKey("recipients.id"))
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.id"))
    event_type = Column(String)
    event_ts = Column(DateTime(timezone=True), default=datetime.utcnow)
    meta = Column(JSON, nullable=True)
