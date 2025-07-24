import json
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

tpl = """
```json
{input_tool_parameters}
```
"""


class Day0Tool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        print(f"Day0Tool - {tool_parameters}")
        text = tpl.format(input_tool_parameters=json.dumps(tool_parameters, indent=2, ensure_ascii=False))
        yield self.create_text_message(text)
        yield self.create_json_message(json=tool_parameters)
