# -*- coding: utf-8 -*-

from datetime import datetime

from core.plugins.get_status_data import get_status_data
from core.plugins.inv.single_host import single_host
# from core.plugins.print_switch_web import print_switch_web
from flask import Flask, render_template
from nornir import InitNornir
from nornir.core import Nornir

from . import app


def get_status(nr: Nornir) -> None:
    # TODO add progressbar
    output = nr.run(get_status_data)
    switches = {}
    for switch in output.keys():
        switches[switch] = output[switch].result
        # return print_switch_web(switches[switch])
        return switches[switch]


@app.route("/")
def home():
    # FIXME
    filter = "f14"
    nr = InitNornir(config_file="nornir_config.yaml")
    nr.inventory.hosts = single_host(nr, filter)
    return render_template("home.html", switch_data=get_status(nr))


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
