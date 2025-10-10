import csv
import json

def csv_to_nested_dict(file_path):
    data = {}
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            semester = row['semestre']
            unite = row['unite']
            module = row['module_name']

            if semester not in data:
                data[semester] = {}
            if unite not in data[semester]:
                data[semester][unite] = {}
            
            data[semester][unite][module] = {
                'unite_title': row['unite_title'],
                'module_title': row['module_title'],
                'coef': int(row['coef']),
                'credit': int(row['credit']),
                'percent_tp': int(row['percent_tp']),
                'percent_td': int(row['percent_td']),
                'percent_exam': int(row['percent_exam'])
            }
    return data


def modules_to_html(data):
    html = [
        '<html><head><meta charset="utf-8">',
        '<style>',
        'body {font-family: Arial; margin: 20px;}',
        'table {border-collapse: collapse; width: 100%; margin-bottom: 20px;}',
        'th, td {border: 1px solid #999; padding: 8px; text-align: left;}',
        'th {background-color: #f2f2f2;}',
        'h2 {color: #2c3e50;}',
        'h3 {color: #16a085;}',
        '</style>',
        '</head><body>'
    ]

    for semester, unites in data.items():
        html.append(f"<h2>Semestre {semester}</h2>")
        for unite, modules in unites.items():
            html.append(f"<h3>Unité: {unite}</h3>")
            html.append("<table>")
            html.append("<tr><th>Code Module</th><th>Titre</th><th>Coef</th><th>Crédit</th>"
                        "<th>TP%</th><th>TD%</th><th>Examen%</th></tr>")
            for module_name, info in modules.items():
                html.append("<tr>")
                html.append(f"<td>{module_name}</td>")
                html.append(f"<td>{info['module_title']}</td>")
                html.append(f"<td>{info['coef']}</td>")
                html.append(f"<td>{info['credit']}</td>")
                html.append(f"<td>{info['percent_tp']}</td>")
                html.append(f"<td>{info['percent_td']}</td>")
                html.append(f"<td>{info['percent_exam']}</td>")
                html.append("</tr>")
            html.append("</table>")
        html.append("<hr>")

    html.append("</body></html>")
    return "\n".join(html)


if __name__ == "__main__":
    filename = "file.csv"

    result = csv_to_nested_dict(filename)
    html_content = modules_to_html(result)

    with open("modules.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Fichier HTML généré : modules.html")
