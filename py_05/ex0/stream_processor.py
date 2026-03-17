
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

del Optional


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "numeric data is invalid"

        if isinstance(data, List):
            count = len(data)
            total = sum(data)
            avg = total / count if count else 0

            result = (f"Processed {count} numeric values, "
                      f"sum={total}, avg={avg:.1f}")
        else:
            result = f"Processed 1 numeric values, sum={data}, avg={data:.1f}"
        return super().format_output(result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, List):
            if not data:
                return False
            for num in data:
                if not isinstance(num, (int, float)):
                    return False
            return True
        elif not isinstance(data, (int, float)):
            return False
        return True


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "text data is invalid"

        chars: int = len(data)
        words: int = len(data.split())

        result = f"Processed text: {chars} characters, {words} words"
        return super().format_output(result)

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return "log data is invalid"

        err = data.split(':')
        if len(err) != 2:
            return "log data is invalid"
        if err[0] == "ERROR":
            result = f"[ALERT] ERROR level detected: {err[1].strip()}"
        elif err[0] == "INFO":
            result = f"[INFO] INFO level detected: {err[1].strip()}"
        return super().format_output(result)

    def validate(self, data: Any) -> bool:
        if data.startswith(("ERROR", "INFO")):
            return True
        return False


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    num_data = [1, 2, 3, 4, 5]
    text_data = "Hello Nexus World"
    log_data = "ERROR: Connection timeout"

    print("\nInitializing Numeric Processor...")
    print(f"Processing data: {num_data}")
    if numeric.validate(num_data):
        print("Validation: Numeric data verified")
    else:
        print("Validation: Numeric data is not verified")
    print(f"{numeric.process(num_data)}")

    print("\nInitializing Text Processor...")
    print(f"Processing data: {text_data}")
    if text.validate(text_data):
        print("Validation: Text data verified")
    else:
        print("Validation: Text data is not verified")
    print(f"{text.process(text_data)}")

    print("\nInitializing Log Processor...")
    print(f"Processing data: {log_data}")
    if log.validate(log_data):
        print("Validation: Log data verified")
    else:
        print("Validation: Log data is not verified")
    print(f"{log.process(log_data)}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface...")

    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data_list: List[Union[int, str, Dict, ]] = [[1, 2, 3],
                                                "Hello Nexus",
                                                "INFO: System ready"]

    for i in range(len(processors)):
        result = processors[i].process(data_list[i])
        result = result.replace("Output: ", "")
        print(f"Result {i+1}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR: ", e)
