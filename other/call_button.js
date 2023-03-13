// Todo: implement filling of forms, explore use of Bluetooth HID dongle, implement touch events in this JS file

// https://saml98.github.io/jekyll/update/2020/10/09/frida-tracing.html
var get_all_views = function() {
    var root = ObjC.classes.UIWindow.keyWindow(); // The root of the view hierarchy
    var buff = [root];                            // The views left to traverse
    var visited = [];                             // The views we have already traversed

    while (buff.length > 0) {
        var node = buff.shift();

        // Make sure we don't traverse a view twice
        if (visited.indexOf(node) >= 0)
            continue;

        visited.push(node);

        // Iterate over all the view's subviews
        var children = node.subviews();

        for (var i=0; i<children.count(); i++) {
            var child = children['- objectAtIndex:'](i);

            if (visited.indexOf(child) == -1)
                buff.push(child);
        }
    }

    return visited;
}

// run for ten minutes max -- this serves as a backup; the script should be quit earlier
var startTime = Date.now();
while ((Date.now() - startTime) < 60000 * 15) {
	// attempt to tap all buttons
	for (v of get_all_views()) {
		if (v // ensure that object still exists; TODO: check if this approach works
			&& typeof v.sendActionsForControlEvents_ !== "undefined") {
			ObjC.schedule(ObjC.mainQueue, function () {
		 		v.sendActionsForControlEvents_(1 <<  6); // UIControlEventTouchUpInside
				console.log("clicked view");
			});

			Thread.sleep(0.5);
		}
	}

	// attempt to close all dialogs
	var nil = ObjC.Object(ptr("0x0"));
	ObjC.schedule(ObjC.mainQueue, function () {
	    ObjC.chooseSync(ObjC.classes.UIAlertController).forEach(element => {
	    	console.log("discarding UIAlertController");
	    	element.dismissViewControllerAnimated_completion_(true, nil);
	    });
	})
}


//var a = new ObjC.Object(ptr('0x159e28340'));

//Module.load("/Library/MobileSubstrate/DynamicLibraries/pccontrol.dylib")

//views = get_all_views()
//get_all_views().forEach(x=>console.log(x.$className));
//buttons = views.filter(function(v) { return v.$className == 'UITabBarButton'; });

/*ObjC.schedule(ObjC.mainQueue, function () {
    ObjC.chooseSync(ObjC.classes.UILabel).forEach(element => {
        element.setText_('Hello World');
    });
})*/


/*var test2;
ObjC.schedule(ObjC.mainQueue, function () {
    ObjC.chooseSync(ObjC.classes.UINavigationController).forEach(element => {
    	console.log("found UINavigationController");
    	test2 = element;
    	element.popViewControllerAnimated_(true);
    });
})

var test3;
ObjC.schedule(ObjC.mainQueue, function () {
    ObjC.chooseSync(ObjC.classes.UINavigationController).forEach(element => {
    	console.log("found UINavigationController");
    	test3 = element;
    	//element.dismissViewControllerAnimated_completion_(true, nil)
    });
})

var test4;
ObjC.schedule(ObjC.mainQueue, function () {
    ObjC.chooseSync(ObjC.classes._UIAlertControllerActionView).forEach(element => {
    	console.log("found _UIAlertControllerActionView");
    	test4 = element;
    	//element.dismissViewControllerAnimated_completion_(true, nil)
    });
}


textfields = views.filter(function(v) { return ['UITextField', 'UISearchBarTextField'].includes(v.$className); });
ObjC.schedule(ObjC.mainQueue, function () {
	if (textfields.length > 0)
		textfields[0].endEditing_(true)
});)*/



	// is button?
	/*
	if (v.$className == 'UILabel') {
		console.log("Found UILabel!");
		console.log(v);
	}*/

	/*var a = new ObjC.Object(ptr(get_all_views()[0].handle));
	if (typeof a.text !== "undefined") {
		a.text().toString();
	}*/

	/*if (['UITextField', 'UISearchBarTextField'].includes(v.$className)) {

		ObjC.schedule(ObjC.mainQueue, function () {
	 		v.setText_('Hello World');
			console.log("set text");
		});

		console.log("Found UITextField!");
		console.log(v);
	}*/