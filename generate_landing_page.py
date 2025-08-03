import os
import yaml

algorithms_dir = "docs/algorithms"
#output_md = "book/index.md"
output_md = "book/workflows.md"
under_dev_url = "../docs/under-development/"

# Load external links (if provided)
with open("algorithm_links.yaml", "r") as f:
    link_config = yaml.safe_load(f)

with open(output_md, "w") as f:
    f.write("# Algorithm Workflow Hub\n\n")
    f.write("Below are links to the available algorithm workflow pages:\n\n")

    for algo, link_type in sorted(link_config.items()):
        if link_type.startswith("http"):
            url = link_type
        elif link_type == "internal":
            html_path = os.path.join(algorithms_dir, algo, "index.html")
            if os.path.isfile(html_path):
                url = f"../docs/algorithms/{algo}/"
            else:
                url = under_dev_url
        else:
            url = under_dev_url

        f.write(f"- [{algo}]({url})\n")

print(f"✅ Landing page written to {output_md}")

