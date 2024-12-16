************************creation********************


Installation et Configuration Django
Installation pip install django.
Création d'un projet: django-admin startproject nomprgt.
Création d'une application: python manage.py startapp nomapp



*************************Testing********************


python manage.py runserver
 =====>  http://127.0.0.1:8000/

python manage.py dbshell

python manage.py makemigrations
python manage.py migrate

C:\Users\DELL\AppData\Local\Programs\Python\Python312\python.exe -m venv venv

changer le hot :
python manage.py runserver 5050







& "C:\Users\DELL\Desktop\2 Drop's\projetD\2droops\venv\Scripts\python.exe" "manage.py" makemigrations
& "C:\Users\DELL\Desktop\2 Drop's\projetD\2droops\venv\Scripts\python.exe" "manage.py" migrate








from django.http import JsonResponse, HttpResponseBadRequest

from django.conf import settings
import os



fa-solid fa-sheet-plastic





  <div class="sidebar pe-4 pb-3">
            <nav class="navbar bg-light navbar-light">
                <a href="{% url 'dashboard' %}" class="navbar-brand mx-4 mb-3">
                    <h3 class="text-primary">2 DROP'S</h3>
                </a>
               
                <div class="navbar-nav w-100">
                    <a href="{% url 'dashboard' %}" class="nav-item nav-link active"><i class="fa fa-tachometer-alt me-2"></i>Dashboard</a>
                    <a href="{% url 'reservation' %}" class="nav-item nav-link"><i class="fa fa-table me-2"></i>Reservations</a>
                    <a href="{% url 'Commandead' %}" class="nav-item nav-link"><i class="fa fa-calendar"></i>Orders</a>
                   
                    <div class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown"><i class="fa fa-money-bill"></i>Transaction</a>
                        <div class="dropdown-menu bg-transparent border-0">
                            <a href="{% url 'Transaction' %}" class="dropdown-item">ON-Line Payment</a>
                            <a href="{% url 'table-datatable' %}" class="dropdown-item">OFF-Line Payment</a>
                        </div>
                    </div>
                   
                   
                   
                   
                    <a href="{% url  'chart' %}" class="nav-item nav-link"><i class="fa fa-chart-bar me-2"></i>Charts</a>
                    <a href="{% url 'app-calender' %}" class="nav-item nav-link"><i class="fa fa-calendar"></i>Calendar</a>


                    <div class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" data-bs-toggle="dropdown"><i class="fa fa-envelope"></i>Emails</a>
                        <div class="dropdown-menu bg-transparent border-0">
                            <a href="{% url 'email-inbox' %}" class="dropdown-item">Inbox</a>
                            <a href="{% url 'email-compose' %}" class="dropdown-item">Compose</a>
                        </div>
                    </div>


                </div>
            </nav>
        </div>







  <a href="{% url 'profile' %}" class="dropdown-item">My Profile</a>
                            <a href="{% url 'ad' %}" class="dropdown-item">Admin Management </a>

                            <a href="{% url 'partenaires' %}" class="dropdown-item">Partner Management </a>
       
                            <a href="{% url 'stations' %}" class="dropdown-item">Station Management </a>
                            <a href="{% url 'categories' %}" class="dropdown-item">Product Management </a>
                            <a href="{% url 'login' %}" class="dropdown-item">Log Out</a>
                        













const express = require('express');
Importe le module express : express est un framework pour Node.js qui simplifie la création de serveurs web. Ici, nous l'utilisons pour créer une instance de l'application Express.



 </div><div class="mb-3">
                                <label for="partenaire" class="form-label">Service	</label>
                               
                              
                          
  {% for s in service %}
                               
                                <div class="form-check">
                                    <input type="checkbox" class="form-check-input" id="{{ s.id_type_etablishment }}" name="service_id" value="{{ s.id_type_etablishment }}" 
                                    >
                                    <label class="form-check-label" for="service_{{ s.id_type_etablishment }}">{{ s.name }}</label>
                                </div>
                               
                                {% endfor %}  </div>








  <div id="funnelChart" style="width: 500px; height: 600px;"></div>

    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script>
        const addresses = {{ addresses|safe }};
        const revenue = {{ revenue|safe }};
        
        const data = [{
            type: "funnel",  
            y: addresses,    
            x: revenue,     
            textinfo: "value+percent initial",  
            marker: {
                color: ['#11a8ef', '#eef7ff', '#fffa89', 
                        '#ffffff', '#6bff6b', '#0d0d0d'],
                line: {
                    color: 'black', 
                    width: 1         
                }
            }
        }];
        
        const layout = {
            title: "Revenue par Adresse", 
            funnelmode: "stack"  
        };
        
        Plotly.newPlot('funnelChart', data, layout);
    </script>



















  command = Commande.objects.prefetch_related("details")

    commandes_with_totals = []
    for commande in command:
        details = commande.details.all()
        total = sum(detail.total_price for detail in details)
        commandes_with_totals.append(
            {"commande": commande, "details": details, "total": total}
        )

    return render(
        request,
        "dashboard/Commandead.html",
        {
            "commandes": commandes_with_totals,
            "total": total,
        },


















def reservation_list(request, id_partenaire):
    partenaire = get_object_or_404(Etablishment, id_partenaire=id_partenaire)
    item = Item.objects.all()
    car = Car.objects.all()
    reservations = Reservation.objects.select_related(
        "id_station", "service_type"
    ).all()
    return render(
        request,
        "dashboard/reservation_part.html",
        {
            "reservations": reservations,
            "partenaire": partenaire,
            "id_partenaire": id_partenaire,
            "item": item,
            "car": car,
        },
    )
























 item = Item.objects.all()
    car = Car.objects.all()
    res = Reservation.objects.select_related(
        "id_station", "service_type"
    ).order_by('-Date')[:3]
    reservations = Reservation.objects.count()
    stations = Station.objects.count()
    orders = Commande.objects.count()
    command = Commande.objects.prefetch_related("details").order_by('-order_date')[:3]

    commandes_with_totals = []
    for commande in command:
        details = commande.details.all()
        total = sum(detail.total_price for detail in details)
        commandes_with_totals.append(
            {"commande": commande, "details": details, "total": total}
        )












'reserv_list' %}" class="nav-item nav-link"><i class="fa fa-table me-2"></i>Reservations</a>
                    <a href="{% url 'command_list'












'reservation_list' id_partenaire=partenaire.id_partenaire %}" class="nav-item nav-link"><i class="fa fa-table me-2"></i>Reservations</a>
                    <a href="{% url 'Commandi' id_partenaire=partenaire.id_partenaire %}"
