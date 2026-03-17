
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, type: str):
        self.stream_id = stream_id
        self.type = type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:

        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "Stream ID": self.stream_id,
            "Type": self.type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        super().__init__(stream_id, "Environmental Data")
        self.sensor_name = "Sensor"

        print(f"\nInitializing {self.sensor_name} Stream...")

    def process_batch(self, data_batch: List[Any]) -> str:

        temps = [float(t) for item in data_batch for value,
                 t in [item.split(':')] if value == "temp"]
        avg_tmp = sum(temps) / len(temps) if temps else 0

        return (f"Sensor analysis: {len(data_batch)} "
                f"readings processed, avg temp: {avg_tmp:.1f}°C")


class TransactionStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        super().__init__(stream_id, "Financial Data")
        self.trans_name = "Transaction"

        print(f"\nInitializing {self.trans_name} Stream...")

    def process_batch(self, data_batch: List[Any]) -> str:

        buy = [int(unit) for item in data_batch for x,
               unit in [item.split(":")] if x == "buy"]
        sell = [int(unit) for item in data_batch for x,
                unit in [item.split(":")] if x == "sell"]

        return (f"Transaction analysis: {len(data_batch)} "
                f"operations, net flow: +{sum(buy) - sum(sell)} units")


class EventStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        super().__init__(stream_id, "System Events")
        self.event_name = "Event"

        print(f"\nInitializing {self.event_name} Stream...")

    def process_batch(self, data_batch: List[Any]) -> str:

        errors = [err for err in data_batch if err == "error"]

        return (f"Event analysis: {len(data_batch)} events, "
                f"{len(errors)} error detected")


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: DataStream = []

    def add_stream(self, stream: DataStream) -> None:
        if not isinstance(stream, DataStream):
            raise TypeError("type stream is invalid")
        self.streams.append(stream)

    def process_streams(self, data: Dict[DataStream, List[Any]]) -> None:
        print("\nBatch 1 Results:")
        for stream, batch in data.items():
            result = stream.process_batch(batch).split(":")[1]
            if isinstance(stream, (EventStream, TransactionStream)):
                print(f"-{stream.type}:", end=" ")
                print(f"{result.split(',')[0].strip()} processed")
            else:
                print(f"-{stream.type}: {result.split(',')[0].strip()}")


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor = SensorStream(" SENSOR_001")
    sen_dic = sensor.get_stats()
    sens_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Stream ID: {sen_dic['Stream ID']}, type: {sen_dic['Type']}")
    print(f"Processing sensor batch: [{', '.join(sens_data)}]")
    analysis = sensor.process_batch(sens_data)
    print(analysis)

    transaction = TransactionStream("TRANS_001")
    trans_dic = transaction.get_stats()
    trans_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Stream ID: {trans_dic['Stream ID']}, Type: {trans_dic['Type']}")
    print(f"Processing event batch: [{', '.join(trans_data)}]")
    analysis = transaction.process_batch(trans_data)
    print(analysis)

    event = EventStream("EVENT_001")
    event_dic = event.get_stats()
    event_data = ["login", "error", "logout"]
    print(f"Stream ID: {event_dic['Stream ID']}, type: {event_dic['Type']}")
    print(f"Processing event batch: [{', '.join(event_data)}]")
    analysis = event.process_batch(event_data)
    print(analysis)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor)
    processor.add_stream(transaction)
    processor.add_stream(event)

    processor.process_streams({
        sensor: ["temp:22.5", "humidity:65"],
        transaction: ["buy:100", "sell:150", "buy:75", "sell:25"],
        event: ["login", "error", "logout"]
    })

    print("\nStream filtering active: High-priority data only")
    sens_data = ["temp:22.5", "humidity:65", "temp:11.5"]
    trans_data = ["buy:100", "sell:150", "buy:75"]
    sensor_filter = sensor.filter_data(sens_data, "temp")
    trans_filter = transaction.filter_data(trans_data, "sell")

    print(f"Filtered results: {len(sensor_filter)} critical", end=" ")
    print(f"sensor alerts, {len(trans_filter)} large transaction")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR: ", e)
