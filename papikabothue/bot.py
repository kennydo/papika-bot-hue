import json
import logging
from typing import (
    Any,
    Dict,
)

import kafka


log = logging.getLogger(__name__)


class PapikaBotHue:
    def __init__(self, config: Dict[str, Any]):
        self.destination_kafka_topic = config['kafka']['to_slack']['topic']
        self.kafka_producer = kafka.KafkaProducer(
            bootstrap_servers=config['kafka']['bootstrap_servers'],
        )

        self.kafka_consumer = kafka.KafkaConsumer(
            config['kafka']['from_slack']['topic'],
            bootstrap_servers=config['kafka']['bootstrap_servers'],
            group_id=config['kafka']['from_slack']['group_id'],
        )

    def run(self):
        for record in self.kafka_consumer:
            raw_message = record.value
            log.debug("Received record: {0}".format(record))

            try:
                wrapped_message = json.loads(raw_message.decode('utf-8'))
            except json.JSONDecodeError:
                log.exception("Could not parse as JSON: {0}".format(raw_message))
                continue

            slack_event = wrapped_message.get('event')
            if not slack_event:
                continue

            if slack_event.get('type') != 'message':
                log.debug("Skipping non-message event")
                continue

            subtype = slack_event.get('subtype')
            if subtype:
                log.debug("Skipping message because it has defined a subtype")
                continue

            log.info("Received Slack event: {0}".format(slack_event))
