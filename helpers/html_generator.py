from typing import Dict, List


class HtmlGenerator:
    def __init__(self, style) -> None:
        self.style: Dict[str, Dict] = style

    def generate_style_in_tag(self, tag_name):
        style_in_tag = 'style = "'
        style: Dict = self.style[tag_name]
        for key in style.keys():
            style_in_tag += f"{key}:{style[key]}; "
        
        style_in_tag += '"'
        return style_in_tag

    def generate_table(self,table_data: List[Dict]) -> str:
        row_count = table_data.__len__()
        table_html = ""
        style_for_td = self.generate_style_in_tag("td")
        for i in range(row_count):
            id = table_data[i]["id"]
            name = table_data[i]["name"]
            price = table_data[i]["price"]
            table_html += f"""
                <tr>
                    <td {style_for_td}>{id}</td>
                    <td {style_for_td}>{name}</td>
                    <td {style_for_td}>{price}</td>
                </tr>
            """
        return table_html