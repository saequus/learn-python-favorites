### Client-side Rendering

This approach allows you to render your structure quickly on the
server-side, then let the user's JavaScript pick up the actual content.

Pros:

- **Quicker perceived user experience**: if there's
enough static content on the initial render, then the user gets their
page back (or at least the beginning of it) quicker and they won't be
bothered about the dynamic content, because in all likelihood that will
render reasonably quickly too.
- **Better control of caching**: By requiring that the
browser makes multiple requests, you can set up your server to use
different caching headers for each URL, depending on your requirements.
In this way, you could allow users to cache the initial page render, but require that a user fetch dynamic (changing) content every time.

Cons:

- **User must have JavaScript enabled**: This is an
obvious one and I shouldn't even need to mention it, but you are cutting out a (very small) portion of your user base if you don't provide a
graceful alternative to your JS-heavy site.
- **Complexity**: This one is a little subjective, but in some ways it's just simpler to have everything in your server-side
language and not require so much back-and-forth. Of course, it can go
both ways.
- **Slow post-processing**: This depends on the browser,
but the fact is that if a lot of DOM manipulation or other
post-processing needs to occur after retrieving the dynamic content, it
might be faster to let the server do it if the server is underutilized.
Most browsers are good at basic DOM manipulation, but if you have to do
JSON parsing, sorting, arithmetic, etc., some of that might be faster on the server.

### Server-side Rendering

This approach allows the user to receive everything at once and also
caters to browsers that don't have good JavaScript support, but it also
means everything takes a bit longer before the browser gets the first `<html>` tag.

Pros:

- **Content appears all at once**: If your server is
fast, it will render everything all at once, and that's that. No messy
XmlHttpRequests (does anyone still use those directly?).
- **Quick post-processing**: Just like you wouldn't want
your application layer to do sorting of a database queryset because the
database is faster, you might also want to reserve a good amount of
processing on the server-side. If you design for the client-side
approach, it's easy to get carried away and put the processing in the
wrong place.

Cons:

- **Slower perceived user experience**: A user won't be
able to see a single byte until the server's work is all done. Sure, the server is probably going to zip through it, but it's still a few extra
seconds on the user's side and you would do them a favor by rendering
what you can right away.
- **Does not scale as well because server spends more time on requests**: It might be that you really want the server to finish a request quickly and move on to the next connection.