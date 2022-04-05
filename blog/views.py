"""views module for blog app"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from authentication.models import User
from authentication.forms import EditProfileForm
from . import forms
from . import models


@login_required
def see_user(request, user_id):
    """_summary_

    Args:
        request (_type_): _description_
        user_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = User.objects.get(id=user_id)
    postes = models.Ticket.objects.filter(user=user)
    number_of_posts = len(postes)
    critiques = models.Critique.objects.filter(user=user)
    number_of_critics = len(critiques)
    following = user.follows.all()
    number_of_following = len(following)
    followers = user.followers.all()
    number_of_followers = len(followers)
    return render(
        request,
        "blog/user_profile.html",
        {
            "user": user,
            "posts": postes,
            "critiques": critiques,
            "number_of_posts": number_of_posts,
            "number_of_critics": number_of_critics,
            "number_of_following": number_of_following,
            "number_of_followers": number_of_followers,
        },
    )


@login_required
def home(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    followed_tickets = models.Ticket.objects.filter(
        user__in=request.user.follows.all()
    ).order_by("-time_created")
    followed_critics = models.Critique.objects.filter(
        user__in=request.user.follows.all()
    ).order_by("-time_created")
    context = {
        "followed_tickets": followed_tickets,
        "followed_critics": followed_critics,
    }
    return render(request, "blog/home.html", context)


@login_required
def posts(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    tickets = models.Ticket.objects.filter(
        user=request.user
        ).order_by(
            "-time_created"
        )
    critiques = models.Critique.objects.filter(user=request.user).order_by(
        "-time_created"
    )
    context = {
        "critiques": critiques,
        "tickets": tickets,
    }
    return render(request, "blog/posts.html", context)


@login_required
def ticket_upload(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    form = forms.TicketForm()
    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect("posts")
    return render(request, "blog/ticket_upload.html", context={"form": form})


@login_required
def critic_response_upload(request, cru_id):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    post = models.Ticket.objects.get(pk=cru_id)
    critique_response = forms.CriticResponseForm()
    if request.method == "POST":
        critique_response = forms.CriticResponseForm(
            request.POST,
            request.FILES
            )
        if critique_response.is_valid():
            cresponse = critique_response.save(commit=False)
            cresponse.user = request.user
            cresponse.ticket = post
            cresponse.save()
            return redirect("home")
    return render(
        request,
        "blog/critique_response_upload.html",
        context={"critique_response": critique_response, "post": post},
    )


@login_required
def standalone_critic(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    ticket = forms.TicketForm()
    critique = forms.CriticResponseForm()
    if request.method == "POST":
        ticket = forms.TicketForm(request.POST, request.FILES)
        critique = forms.CriticResponseForm(request.POST, request.FILES)
        if ticket.is_valid() and critique.is_valid():
            ticket = ticket.save(commit=False)
            ticket.user = request.user
            ticket.save()
            critique = critique.save(commit=False)
            critique.user = request.user
            critique.ticket = ticket
            critique.save()
            return redirect("home")
    return render(
        request,
        "blog/standalone_critic.html",
        context={"ticket": ticket, "critique": critique},
    )


@login_required
def edit_ticket(request, ticket_id):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    ticket = models.Ticket.objects.get(pk=ticket_id)
    form = forms.TicketForm(instance=ticket)

    if request.method == "POST":
        form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect("posts")
    return render(
        request,
        "blog/edit_ticket.html",
        context={
            "form": form,
            "ticket": ticket,
        },
    )


@login_required
def edit_critic(request, critique_id):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    critique = models.Critique.objects.get(pk=critique_id)
    form = forms.CriticResponseForm(instance=critique)

    if request.method == "POST":
        form = forms.CriticResponseForm(
            request.POST,
            request.FILES,
            instance=critique
        )
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(
        request,
        "blog/edit_critic.html",
        context={
            "form": form,
            "critique": critique
        },
    )


@login_required
def edit_profile(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        form = EditProfileForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect(
                "user_profile",
                user_id=request.user.id
            )

    else:
        form = EditProfileForm(instance=request.user)
        args = {"form": form}
        return render(request, "blog/edit_profile.html", args)


@login_required
def delete_ticket(request, user_id):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        pass
    else:
        ticket = models.Ticket.objects.get(pk=user_id)
        ticket.delete()
        return redirect("posts")


@login_required
def delete_critic(request, user_id):
    """_summary_

    Args:
        request (_type_): _description_
        pk (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        pass
    else:
        critique = models.Critique.objects.get(pk=user_id)
        critique.delete()
        return redirect("posts")


@login_required
def abonnements(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    user = request.user
    followers = user.followers.all()
    follows = user.follows.all()
    if request.method == "POST":
        if request.POST.get("follow"):
            if request.POST.get("follow") == user.username:
                return render(
                    request,
                    "blog/abonnements.html",
                    {
                        "followers": followers,
                        "follows": follows,
                        "error": "Vous ne pouvez pas vous suivre vous même!",
                    },
                )

            elif request.POST.get("follow") in [
                follower.username for follower in follows
            ]:
                return render(
                    request,
                    "blog/abonnements.html",
                    {
                        "followers": followers,
                        "follows": follows,
                        "error": "Vous suivez déjà cet utilisateur!",
                    },
                )
            else:
                followed_user = User.objects.get(
                    username=request.POST.get("follow")
                )
                user.follows.add(followed_user)
                follows = user.follows.all()
                return render(
                    request,
                    "blog/abonnements.html",
                    {
                        "followers": followers,
                        "follows": follows,
                        "success": "Vous suivez maintenant "
                        + followed_user.username,
                    },
                )
        if request.POST.get("unfollow"):
            user.follows.remove(
                User.objects.get(
                    pk=request.POST.get("unfollow")
                )
            )
            return render(
                request,
                "blog/abonnements.html",
                {
                    "followers": followers,
                    "follows": follows,
                    "success": "Votre abonnement a été supprimé",
                },
            )
    return render(
        request,
        "blog/abonnements.html",
        {
            "followers": followers,
            "follows": follows
        },
    )
