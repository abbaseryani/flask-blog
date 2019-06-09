from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    hello="hello world"
    forms = [
        {
            "header": "Request ARP (Assay Ready Plates)",
            "desc": "Primary Screen: minimum of 5 days notice, HC & HP: <100 cpds, minimum of 72h notice is required HC & HP: >100 cpds, please ask CM for schedule",
            "buttons": [
                {
                    "value": "Primary screen and Hit confirmation",
                    "onclick": "redirectARP()"
                },
                {
                    "value": "Hit profiling 11pt (DF: 1.65 or 2)",
                    "onclick": "redirect1_2_ARP()"
                },
                {
                    "value": "Hit profiling 10pt (DF: 3 or 3/3.33)",
                    "onclick": "redirect3_13_ARP()"
                },
                {
                    "value": "Hit profiling 5pt (DF: 3)",
                    "onclick": "redirect3_8_13_18_ARP()"
                }
                        ]
        },
        {
            "header": "Request NARP (Near Assay Ready Plates)",
            "desc": "Primary Screen: minimum of 5 days notice, HC & HP: <100 cpds, minimum of 72h notice is required HC & HP: >100 cpds, please ask CM for schedule",
            "buttons": [
                {
                    "value": "Primary screen and Hit confirmation",
                    "onclick": "redirectNARP()"
                },
                {
                    "value": "Hit profiling 11pt (DF: 1.65 or 2)",
                    "onclick": "redirect1_2_NARP()"
                },
                {
                    "value": "Hit profiling 10pt (DF: 3 or 3/3.33)",
                    "onclick": "redirect3_13_NARP()"
                },
                {
                    "value": "Hit profiling 5pt (DF: 3)",
                    "onclick": "redirect3_8_13_18_NARP()"
                }
                       ]
        },
        {
            "header": "Request Aliquots",
            "desc": "minimum of 48hrs notice is required",
            "buttons": [
                {
                    "value": "Aliquots for External customer compounds",
                    "onclick": "redirectAliquot()"
                }
            ]
        },
        {
            "header": "Request Template Replication (Spotting Request)",
            "desc": "minimum of 24hrs notice is required",
            "buttons": [
                {
                    "value": "Template Replication (Spotting Request)",
                    "onclick": "redirectSpotting()"
                }
            ]
        },
        {
            "header": "Request Barcodes",
            "desc": "minimum of 72hrs notice is required",
            "buttons": [
                {
                    "value": "Plates Label",
                    "onclick": "platesLabel()"
                },
                {
                    "value": "Print Barcodes",
                    "onclick": "printBarcode()"
                }
            ]
        }

    ]
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, forms=forms, hello=hello)


@main.route("/about")
def about():
    return render_template('about.html', title="About")


@main.route("/test")
def test():
    return render_template('test.html', title="test")
